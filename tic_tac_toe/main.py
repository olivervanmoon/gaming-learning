# tic tac toe

from game import Game
from board import Board
from player import Player

board = Board()

player1 = Player('Oliver', 'x')
player2 = Player('Niko', 'o')

players = [player1, player2]

game = Game(board, players)

game.play()