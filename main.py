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

players = ['Bart', 'Ter', 'Nop', 'Mac']

sess = PokerSession(players)
sess.buyin("ter", "mac", 50)
sess.buyin("mac", "bart", 50)
sess.buyin("ter", "mac", 50)
sess.buyin("mac", "bart", 50)
sess.buyin("ter", "bart", 35)
sess.buyin("ter", "mac", 15)
sess.buyin("bart", "mac", 50)
sess.buyin("mac", "bart", 50)
sess.buyin("ter", "bart", 50)
sess.buyin("ter", "bart", 50)
sess.buyin("ter", "bart", 50)
sess.buyin("ter", "bart", 50)
sess.buyin("ter", "bart", 50)
sess.buyin("mac", "ter", 50)
sess.buyin("bart", "ter", 39)
sess.buyin("bart", "mac", 21)
sess.buyin("bart", "mac", 50)
sess.buyin("bart", "mac", 30)
sess.buyin("bart", "ter", 10)
sess.buyin("ter", "mac", 50)
sess.buyin("mac", "bart", 50)
sess.buyin("bart", "mac", 50)
sess.buyin("bart", "mac", 45)
sess.buyin("bart", "ter", 5)
sess.buyin("bart", "mac", 50)
sess.buyin("ter", "mac", 50)
sess.buyin("bart", "mac", 50)
sess.buyin("ter", "mac", 5)
sess.buyin("bart", "mac", 15)
sess.buyin("bart", "ter", 50)
sess.buyin("mac", "ter", 50)

sess.getSummary()

22:10 Nop 黃俊城 ter tid nop 25
22:10 Nop 黃俊城 ter tid bart 20
22:10 Nop 黃俊城 ter tid mac 5
22:12 Nop 黃俊城 nop tid bart 50
22:14 Nop 黃俊城 mac tid ter 35
22:14 Nop 黃俊城 mac tid bart 15
22:22 Nop 黃俊城 nop tid ter 50
22:23 Nop 黃俊城 bart tid ter 30
22:23 Nop 黃俊城 bart tid mac 20
22:25 Nop 黃俊城 bart tid ter 45
22:25 Nop 黃俊城 bart tid mac 5
22:27 Nop 黃俊城 mac tid bart 50
22:32 Nop 黃俊城 ter tid bart 50
22:33 Nop 黃俊城 nop tid ter 50
22:38 Nop 黃俊城 bart tid ter 50
22:38 Nop 黃俊城 mac tid ter 50
22:40 Nop 黃俊城 bart tid ter 50
22:44 Nop 黃俊城 nop tid bart 45
22:44 Nop 黃俊城 nop tid mac 5
22:46 Nop 黃俊城 bart tid ter 30
22:47 Nop 黃俊城 barti tid mac 20
22:49 Nop 黃俊城 mac tid ter 40
22:49 Nop 黃俊城 mac tid bart 10
22:50 Nop 黃俊城 bart tid ter 50
22:51 Nop 黃俊城 nop tid bart 50
22:53 Ter Photos
22:53 Ter Lag kanard kid wa gu yung yu nai call
22:54 Ter Lol
22:56 Nop 黃俊城 bart tid ter 50
23:03 Nop 黃俊城 nop tid mac 50
23:04 Nop 黃俊城 ter tid bart 50
23:05 Nop 黃俊城 nop tid bart 50
23:08 Nop 黃俊城 nop tid bart 50
23:10 Nop 黃俊城 mac tid bart 50
23:11 Nop 黃俊城 mac tid ter 50
23:24 Nop 黃俊城 bart tid nop 50
23:25 Nop 黃俊城 ter tid nop 30
23:25 Nop 黃俊城 ter tid bart 10
23:25 Nop 黃俊城 ter tid mac 10
23:28 Ter Bart?
23:29 Bart phone overgeat
23:29 Bart dai la
23:37 Nop 黃俊城 mac tid bart 50
23:37 Nop 黃俊城 nop tid bart 50
23:38 Nop 黃俊城 ter tid bart 50
23:39 Bart Photos
23:39 Bart gu tong use nee puer hai phone yen long rew
23:40 Nop 黃俊城 https://developer.mozilla.org/en-US/docs/Web/API/Blob
23:43 Nop 黃俊城 ['Nop owe Mac: 55',
'Mac owe Ter: 160',
'Nop owe Ter: 45',
'Bart owe Ter: 125',
'Mac owe Bart: 130',
'Nop owe Bart: 245']
