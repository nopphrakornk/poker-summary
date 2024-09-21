import json
import requests
import logging
from flask import Flask, request, jsonify
from google.cloud import firestore
from pokerbot import (
    start_session,
    check_ongoing_session,
    start_session,
    end_session,
    extract_transaction_details,
    update_money_owed_and_players,
    get_secret,
)

app = Flask(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler()],
)

LINE_CHANNEL_ACCESS_TOKEN = get_secret("LINE_CHANNEL_ACCESS_TOKEN")

db = firestore.Client()

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


def reply_message(reply_token, text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}",
    }
    data = {"replyToken": reply_token, "messages": [{"type": "text", "text": text}]}
    url = "https://api.line.me/v2/bot/message/reply"
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code != 200:
        logging.error(
            f"ERROR: Failed to send message: {response.status_code} - {response.text}"
        )


@app.route("/webhook", methods=["POST"])
def webhook(request):
    try:
        body = request.get_json()

        if not body:
            logging.error("No body received")
            return jsonify({"status": "Error", "message": "No body received"}), 400

        events = body.get("events", [])
        if not events:
            logging.warning("No events found in the body")
            return jsonify({"status": "OK"}), 200

        for event in events:
            if event.get("type") == "message":
                reply_token = event.get("replyToken")
                message = event.get("message", {})
                message_text = message.get("text", "")
                message_text = message_text.lower()
                ongoing_session_id = check_ongoing_session(db)
                response_text = None
                if ongoing_session_id:
                    if "tid" in message_text:
                        result = extract_transaction_details(message_text)
                        if result:
                            person1, person2, amount = result
                            response_text = update_money_owed_and_players(
                                ongoing_session_id, person1, person2, amount, db
                            )
                        else:
                            response_text = "Did not update money."
                    else:
                        response_text = "There's an ongoing poker session!"

                if "pokerbot" in message_text:
                    if "start" in message_text:
                        response_text = start_session(db)
                    elif "end" in message_text:
                        response_text = end_session(db)
                    else:
                        response_text = "How can I help you?"
                if response_text:
                    reply_message(reply_token, response_text)

        return jsonify({"status": "OK"}), 200
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"status": "Error", "message": str(e)}), 500


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8080)
