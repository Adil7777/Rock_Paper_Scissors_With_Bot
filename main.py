from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
import sys
import random


class Game(QMainWindow):
    def __init__(self):
        super(Game, self).__init__()
        loadUi('rockpaper.ui', self)

        self.paper.clicked.connect(self.winner_paper)
        self.rock.clicked.connect(self.winner_rock)
        self.scissors.clicked.connect(self.winner_scissors)

    @pyqtSlot()
    def winner_rock(self):
        winner, bots_move = check_winner('rock')
        self.winner.setText(str(winner))
        self.bot.setText('Bots move is: ' + bots_move)

    @pyqtSlot()
    def winner_paper(self):
        winner, bots_move = check_winner('paper')
        self.winner.setText(str(winner))
        self.bot.setText('Bots move is: ' + bots_move)

    @pyqtSlot()
    def winner_scissors(self):
        winner, bots_move = check_winner('scissors')
        self.winner.setText(str(winner))
        self.bot.setText('Bots move is: ' + bots_move)


def get_bots_move():
    return random.choice(['rock', 'paper', 'scissors'])


# print(get_bots_move())

def check_winner(users_move):
    bots_move = get_bots_move()
    print(bots_move)

    if bots_move == users_move:
        return 'Tie game', bots_move

    elif bots_move == 'rock':
        if users_move == 'paper':
            return 'User won', bots_move
        else:
            return 'Bot won', bots_move

    elif bots_move == 'scissors':
        if users_move == 'paper':
            return 'Bot won', bots_move
        else:
            return 'User won', bots_move

    elif bots_move == 'paper':
        if users_move == 'rock':
            return 'Bot won', bots_move
        else:
            return 'User won', bots_move


# print(check_winner('rock'))


app = QApplication(sys.argv)
window = Game()
window.show()
try:
    sys.exit(app.exec_())
except:
    print('exit')
