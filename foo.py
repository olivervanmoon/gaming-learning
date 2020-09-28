import numpy as np

board = np.array([
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
])



def winner(board, n):
    c = 0
    for i, row in enumerate(board):
        for j, _ in enumerate(row):
            print(i,j)

            def col():
                coord[0] += 1

            def row():
                coord[1] += 1

            def diag():
                coord[0] += 1
                coord[1] += 1

            def anti():
                coord[0] += 1
                coord[1] -= 1

            wintypes = [col, row, diag, anti]

            for wintype in wintypes:
                print('testing wintype ' + wintype.__name__)
                coord = [i,j]
                while coord[0] < np.size(board,0) and coord[1] < np.size(board,1):
                    if board[tuple(coord)] == 1:
                        c += 1
                        print('it\'s a 1! count is now ' + str(c))
                        if c == self.n:
                            print('hit target!!!')
                            return True
                        wintype() # go to next square
                    else:
                        print('not a 1')
                        c = 0
                        break
                print('going to next win type')
            print('going to next square in for loop')
    return False

status = winner(board, 3)
print()
print(status)
print()