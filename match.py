import random

output = list('AABBCCDD')
random.shuffle(output)
output = [output[:4], output[4:8]]
board = [list('*'*4) for i in range(2)]

def check():
    x1,y1 = map(int, input('Input position: '))
    print_board((x1,y1))
    x2,y2 = map(int, input('Input position: '))
    print_board((x1,y1),(x2,y2))
    if output[x1][y1] == output[x2][y2]:
        print('Match!!')
        board[x1][y1] = output[x1][y1]
        board[x2][y2] = output[x2][y2]
    else:
        print('Failed!!')
    if any('*' in row for row in board):
        return True

def print_board(*pic):
    for row in range(len(output)):
        for col in range(len(output[0])):
            if (row,col) in pic:
                print(output[row][col], end='')
            else:
                print(board[row][col], end='')
        print()

print_board()

while check():
    pass

print('Done!')
