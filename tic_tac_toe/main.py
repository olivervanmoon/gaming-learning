# tic tac toe
# Oliver van Moon

from game import Game
from board import Board
from player import HumanPlayer, StupidRandomPlayer, SmarterRandomPlayer

board = Board(3,3) # rows, cols

player1 = HumanPlayer('Oliver', 'o')
#player2 = HumanPlayer('Niko', 'n')
#player2 = StupidRandomPlayer('Rando', 'r')
player2 = SmarterRandomPlayer('SmarterRando', 'r')

players = [player1, player2]

game = Game(board, players, 3) # "n in a row"

game.play()