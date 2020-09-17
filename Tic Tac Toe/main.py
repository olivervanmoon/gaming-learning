# tic tac toe

from game import Game
from board import Board
from player import Player

board = Board()

player1 = Player('Oliver', 'x', 69)
player2 = Player('Niko', 'o', 420)

print('player1 id is: ')
print(id(player1))

players = [player1, player2]

game = Game(players)

board.display()
while board.squareLeft():
	position = game.currentPlayer.getMove(board, game)
	board.move(game.currentPlayer.id, position)
	game.ply += 1
	board.display()
	if game.winner(board):
		break
	game.switchPlayer()
game.endMessage(board)

for player in players:
	print(player.age)