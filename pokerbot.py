import re
from google.cloud import firestore, secretmanager


def get_secret(secret_id):
    name = f"projects/webhooktest-435712/secrets/{secret_id}/versions/latest"
    secret_client = secretmanager.SecretManagerServiceClient()
    secret_response = secret_client.access_secret_version(request={"name": name})
    secret_value = secret_response.payload.data.decode()
    secret_value = secret_value.split("=", 1)[1].strip().strip("'")
    return secret_value


def check_ongoing_session(firestore_db):
    ongoing_session_query = (
        firestore_db.collection("pokerSession").where("inSession", "==", True).limit(1)
    )
    ongoing_session = ongoing_session_query.stream()
    for doc in ongoing_session:
        return doc.id
    return False


def start_session(firestore_db):
    ongoing_session_id = check_ongoing_session(firestore_db)

    if ongoing_session_id:
        return f"An active session already exists with session_id: {ongoing_session_id}"  # Return the ongoing session's document ID

    doc_ref = firestore_db.collection("pokerSession").document()

    data = {
        "sessionStartTime": firestore.SERVER_TIMESTAMP,  # Use server timestamp for accuracy
        "inSession": True,
        "players": [],
        "pairwiseMoneyOwed": {},
    }

    doc_ref.set(data)
    return f"New session started with session_id: {doc_ref.id}"


def end_session(firestore_db):
    ongoing_session_id = check_ongoing_session(firestore_db)

    if not ongoing_session_id:
        return "No active session found to end."

    doc_ref = firestore_db.collection("pokerSession").document(ongoing_session_id)

    data = {
        "sessionEndTime": firestore.SERVER_TIMESTAMP,  # Record the session end time
        "inSession": False,
    }

    doc_ref.update(data)
    response_txt = summarize_money_owed(ongoing_session_id, firestore_db)
    return f"{response_txt} \n Session ended for session_id: {doc_ref.id}"


def update_money_owed_and_players(session_id, payer, payee, amount, firestore_db):
    doc_ref = firestore_db.collection("pokerSession").document(session_id)

    doc_snapshot = doc_ref.get()
    if doc_snapshot.exists:
        session_data = doc_snapshot.to_dict()
        players = session_data.get("players", [])
        pairwise_money_owed = session_data.get("pairwiseMoneyOwed", {})

    updated = False
    if payer not in players:
        players.append(payer)
        updated = True
    if payee not in players:
        players.append(payee)
        updated = True

    if updated:
        doc_ref.update({"players": players})
        print(f"Updated player list in session {session_id}: {players}")

    if payer not in pairwise_money_owed:
        pairwise_money_owed[payer] = {}
    if payee not in pairwise_money_owed[payer]:
        pairwise_money_owed[payer][payee] = 0.0

    pairwise_money_owed[payer][payee] += amount

    doc_ref.update(
        {f"pairwiseMoneyOwed.{payer}.{payee}": pairwise_money_owed[payer][payee]}
    )
    return f"Done updating: {payer} -> {payee}: {amount}"


def summarize_money_owed(session_id, firestore_db):
    doc_ref = firestore_db.collection("pokerSession").document(session_id)

    doc_snapshot = doc_ref.get()

    session_data = doc_snapshot.to_dict()

    pairwise_money_owed = session_data.get("pairwiseMoneyOwed", {})
    net_balances = {}
    for payer, owes in pairwise_money_owed.items():
        if payer not in net_balances:
            net_balances[payer] = 0
        for payee, amount in owes.items():
            if amount > 0:
                net_balances[payer] -= amount
                if payee not in net_balances:
                    net_balances[payee] = 0
                net_balances[payee] += amount

    creditors = {
        player: balance for player, balance in net_balances.items() if balance > 0
    }
    debtors = {
        player: -balance for player, balance in net_balances.items() if balance < 0
    }

    transactions = []

    while creditors and debtors:
        creditor, credit_amount = creditors.popitem()
        debtor, debt_amount = debtors.popitem()

        if credit_amount > debt_amount:
            transactions.append(f"{debtor} owes {creditor} {debt_amount:.2f}")
            creditors[creditor] = credit_amount - debt_amount
        elif credit_amount < debt_amount:
            transactions.append(f"{debtor} owes {creditor} {credit_amount:.2f}")
            debtors[debtor] = debt_amount - credit_amount
        else:
            transactions.append(f"{debtor} owes {creditor} {credit_amount:.2f}")

    if len(transactions) == 0:
        return "EVERYBODY IS BALANCED OUT!" + "\n" + str(net_balances)
    return "\n".join(transactions) + "\n" + str(net_balances)


def extract_transaction_details(text):
    pattern = r"(\w+(?:\s\w+)*)\s+tid\s+(\w+(?:\s\w+)*)\s+(\d+(?:\.\d+)?)"
    match = re.search(pattern, text)
    if match:
        person1 = match.group(1)
        person2 = match.group(2)
        amount = float(match.group(3))
        return person1, person2, amount
    else:
        return None
