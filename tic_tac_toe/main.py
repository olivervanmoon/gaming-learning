# tic tac toe
# Oliver van Moon

from game import Game
from board import Board
from player import HumanPlayer, RandomPlayer

board = Board(3,3) # rows, cols (but game can't check for larger than 3x3 yet)

player1 = HumanPlayer('Oliver', 'o')
#player2 = HumanPlayer('Niko', 'n')
player2 = StupidRandomPlayer('Rando', 'r')

players = [player1, player2]

game = Game(board, players)

game.play()