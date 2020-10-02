# tic tac toe
# Oliver van Moon

from game import Game
from board import Board
from player import HumanPlayer, RandomPlayer

board = Board(3,3) # rows, cols

oli = HumanPlayer('Oliver', 'o')
niko = HumanPlayer('Niko', 'n')
rando = RandomPlayer('Rando', 'r')

players = [oli, rando]

game = Game(board, players, 3) # "n in a row"

game.play()