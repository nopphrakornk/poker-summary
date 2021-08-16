import numpy as np


class PokerSession():
    def __init__(self, players_list):
        players_list = players
        self.players_list = players_list
        self.n_players = len(players)
        self.money_grid = np.zeros((self.n_players, self.n_players))
        self.owe = np.zeros((self.n_players, self.n_players))

    def add_player(self, new_player):
        # np.zeros(self.n_players)
        self.money_grid = np.pad(self.money_grid, pad_width = [(0,1), (0,1)])
        self.players_list.append(new_player)

    def buyin(self, buyer, seller, amount):
        self.money_grid[self.players_list.index(buyer.capitalize()), self.players_list.index(seller.capitalize())] += amount

    def getSummary(self):
        lines = list()
        print('Raw:')
        for row in range(self.n_players):
            for col in range(self.n_players):
                if row == col:
                    pass
                else:
                    lose_minus_win = self.money_grid[row, col] - self.money_grid[col, row]
                    if lose_minus_win < 0:
                        temp = '{loser} owe {winner}: {amount}'.format(loser = players[col], winner =  players[row], amount = int(np.abs(lose_minus_win)))
                        print(temp)
                        lines.append(temp)
                        self.owe[col, row] = lose_minus_win*-1

        checker = list()
        for i in range(self.n_players):
            profit_loss = self.money_grid[:,i].sum() - self.money_grid[i,:].sum()
            checker.append(profit_loss)

        print('==========================')

        print('What to transfer:')
        for i in range(self.n_players):
            max_cost, max_earn = self.owe[i].argmax(), self.owe[:,i].argmax()
            if self.owe[max_earn, i] - self.owe[i, max_cost] > 0:
                self.owe[max_earn, max_cost] += self.owe[i,max_cost]
                self.owe[max_earn, i] -= self.owe[i,max_cost]
                self.owe[i,max_cost] -= self.owe[i,max_cost]
            elif self.owe[max_earn, i] - self.owe[i, max_cost] <= 0:
                self.owe[max_earn, max_cost] += self.owe[max_earn,i]
                self.owe[i, max_cost] -= self.owe[max_earn, i]
                self.owe[max_earn, i] -= self.owe[max_earn, i]

        simp_lines = list()
        for i in range(self.n_players):
            for j in range(self.n_players):
                if self.owe[i,j] != 0:
                    temp = self.players_list[i] + ' owe ' + self.players_list[j] + ' '+ str(self.owe[i,j])
                    print(temp)
                    simp_lines.append(temp)

        print('++++++++++++++++++++++++++')
        checker2 = list()
        for i in range(self.n_players):
            profit_loss = self.owe[:,i].sum() - self.owe[i].sum()
            checker2.append(profit_loss)

        if checker == checker2:
            for i in range(self.n_players):
                print(self.players_list[i] + ' should get '+ str(checker[i]))
        else:
            print('Something\'s wrong...')
        return checker2, simp_lines

        
players = ['Nop', 'Mac', 'Ter']

sess = PokerSession(players)
sess.buyin("mac", "ter", 25)
sess.buyin("mac", "nop", 25)
sess.buyin("nop", "mac", 50)
sess.buyin("mac", "nop", 25)
sess.buyin("nop", "mac", 50)
sess.buyin("mac", "nop", 25)
sess.buyin("nop", "mac", 50)
sess.buyin("mac", "nop", 25)

a = sess.getSummary()
