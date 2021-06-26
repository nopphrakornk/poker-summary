import numpy as np


class PokerSession():
    def __init__(self, players_list):
        players_list = players
        self.players_list = players_list
        self.n_players = len(players)
        self.money_grid = np.zeros((self.n_players, self.n_players))

    def add_player(self, new_player):
        np.zeros(self.n_players)
        self.money_grid = np.pad(self.money_grid, pad_width = [(0,1), (0,1)])
        self.players_list.append(new_player)

    def buyin(self, buyer, seller, amount):
        self.money_grid[self.players_list.index(buyer), self.players_list.index(seller)] += amount

    def getSummary(self):
        lines = list()
        for row in range(len(self.players_list)):
            for col in range(len(self.players_list)):
                if row == col:
                    pass
                else:
                    lose_minus_win = self.money_grid[row, col] - self.money_grid[col, row]
                    if lose_minus_win < 0:
                        lines.append('{loser} owe {winner}: {amount}'.format(loser = players[col], winner =  players[row], amount = int(np.abs(lose_minus_win))))
        return lines

players = ['Mac', 'Ter', 'Nop']

sess = PokerSession(players)
sess.buyin('Ter', 'Nop', 50)
sess.buyin('Mac', 'Ter', 100)
sess.buyin('Mac', 'Ter', 50)
sess.buyin('Nop', 'Ter', 50)
sess.buyin('Mac', 'Ter', 50)
sess.buyin('Nop', 'Ter', 50)
sess.buyin('Nop', 'Mac', 50)
sess.buyin('Mac', 'Nop', 50)
sess.buyin('Ter', 'Mac', 50)
sess.buyin('Ter', 'Nop', 50)
sess.buyin('Mac', 'Nop', 7.5)

print(sess.getSummary())
