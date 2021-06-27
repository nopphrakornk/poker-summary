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
        self.money_grid[self.players_list.index(buyer.capitalize()), self.players_list.index(seller.capitalize())] += amount

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

players = ['Mac', 'Ter', 'Nop', 'Bart']

sess = PokerSession(players)


sess.buyin("Bart","ter", 50)
sess.buyin("Nop","ter", 50)
sess.buyin("Ter","mac", 25)
sess.buyin("Ter","nop", 25)
sess.buyin("Ter","mac", 25)
sess.buyin("BaRt","nop", 25)
sess.buyin("Bart","ter", 25)
sess.buyin("Ter","mac", 50)
sess.buyin("Nop","ter", 50)
sess.buyin("Nop","ter", 50)
sess.buyin("Ter","bart", 50)
sess.buyin("Nop","ter", 50)
sess.buyin("Nop","mac", 50)
sess.buyin("Ter","mac", 50)
sess.buyin("Ter","nop", 25)
sess.buyin("Ter","bart", 25)
sess.buyin("mac","nop", 25)
sess.buyin("mac","ter", 25)
sess.buyin("Ter","nop", 50)
sess.buyin("Bart","mac", 25)
sess.buyin("Bart","nop", 25)
sess.buyin("Bart","nop", 50)
sess.buyin("mac","ter", 50)
sess.buyin("bart","nop", 50)
sess.buyin("Ter","mac", 50)
sess.buyin("Nop","mac", 50)
sess.buyin("Nop","ter", 50)
sess.buyin("Bart","mac", 50)
sess.buyin("Nop","bart", 50)
sess.buyin("ter","mac", 50)
sess.buyin("Bart","ter", 50)
sess.buyin("Nop","mac", 50)
sess.buyin("Nop","mac", 25)
sess.buyin("Bart","ter", 50)
sess.buyin("Bart","ter", 50)
sess.buyin("Nop","bart", 25)
sess.buyin("Nop","ter", 25)
sess.buyin("Ter","bart", 50)
sess.buyin("Ter","bart", 50)
sess.buyin("Nop","bart", 25)
sess.buyin("Nop","mac", 25)
sess.buyin("Ter","mac", 50)
sess.buyin("Mac","nop", 25)
sess.buyin("Mac","ter", 25)
sess.buyin("ter","bart", 50)
sess.buyin("Nop","bart", 50)
sess.buyin("Bart","mac", 50)
sess.buyin("Ter","nop", 25)
sess.buyin("Ter","mac", 25)
sess.buyin("Bart","mac", 50)
sess.buyin("Ter","mac", 7.5)
sess.buyin("Nop","ter", 32.25)
sess.buyin("Nop", "mac", 50)
sess.buyin("bart", "mac", 50)
sess.buyin("ter", "mac", 50)

#pokdeng starts here
sess.buyin("ter", "mac", 100)
sess.buyin("bart", "mac", 100)
sess.buyin("nop", "mac", 100)


sess.buyin("mac", "bart", 50)
sess.buyin("nop", "bart", 50)
sess.buyin("ter", "bart", 50)

sess.buyin("mac", "bart", 50)
sess.buyin("nop", "bart", 50)
sess.buyin("ter", "bart", 50)

sess.buyin("mac", "bart", 50)
sess.buyin("nop", "bart", 50)
sess.buyin("ter", "bart", 50)


sess.buyin("nop", "Ter", 100)
sess.buyin("bart", "Ter", 100)
sess.buyin("mac", "Ter", 100)

sess.getSummary()
