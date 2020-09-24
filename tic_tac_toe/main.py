# tic tac toe

from game import Game
from board import Board
from player import Player

board = Board(3,3) # rows, cols (but game can't check for larger than 3x3 yet)

player1 = Player('Oliver', 'o')
player2 = Player('Niko', 'n')

players = [player1, player2]

game = Game(board, players)

game.play()