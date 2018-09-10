# Game Board class
import random

class GameBoard():
    def __init__(self):
        # Check for valid size later on
        self.size  = int ( input("Enter size (n x n): ") ) # Clear up description
        self.nMines = int( input("Enter the number of mines: ") )
        self.board = self.generate_board()



    def generate_board(self):
    # Generate a blank board
        board = [['-' for i in range(0, self.size)] for j in range(0, self.size)]

        # Revealed Board
        rBoard = [[False for i in range(0, self.size)] for j in range(0, self.size)]

        mCounter = self.nMines
        while mCounter > 0:
            i = random.randint(0, self.size - 1)
            j = random.randint(0, self.size - 1)

            if board[i][j] == '-':
                board[i][j] = 'M'
                mCounter = mCounter - 1
        return board

    # Check to see if a specific cell is revealed
    def is_revealed(self, i, j):
        return rBoard[i][j]

    # Mark a cell as revealed
    def mark_revealed(self, i, j):
        rBoard[i][j] = True


    # Prints out the board one row at a time
    def print_board(self):
        for i in self.board:
            print(i)

    def a(self, i, j):
        if self.board[i][j] == 'M':
            return 1
        else:
            return 0

    def f(self, i, j):
        d = {'U' : False, 'U_L' : False, 'U_R' : False,
                      'D' : False, 'D_L' : False, 'D_R' : False,
                      'L' : False, 'R'   : False}

        c = 0

        # Up
        if ((i - 1) >= 0):
            d['U'] = self.board[i-1][j]
            c = c + self.a((i-1),(j))

        # Up Left
        if ((i - 1) >= 0) and ((j - 1) >= 0):
            d['U_L'] = self.board[i-1][j-1]
            c = c + self.a((i-1),(j-1))

        # Up Right
        if ((i - 1) >= 0) and ((j + 1) < self.size):
            d['U_R'] = self.board[i-1][j+1]
            c = c + self.a((i-1),(j+1))

        # Down
        if (i + 1) < self.size:
            d['D'] = self.board[i+1][j]
            c = c + self.a((i+1),(j))

        # Down Left
        if ((i + 1) < self.size) and ((j - 1) >= 0):
            d['D_L'] = self.board[i+1][j-1]
            c = c + self.a((i+1),(j-1))

        # Down Right
        if ((i + 1) < self.size) and ((j + 1) < self.size):
            d['D_R'] = self.board[i+1][j+1]
            c = c + self.a((i+1),(j+1))

        # Left
        if (j - 1) >= 0:
            d['L'] = self.board[i][j-1]
            c = c + self.a((i),(j-1))

        # Right
        if (j + 1) < self.size:
            d['R'] = self.board[i][j+1]
            c = c + self.a((i),(j+1))

        return(c)

    def mark_adjacent(self):
        iN = 0
        jN = 0

        for i in self.board:
            for j in i:
                c = 0
                if j != 'M':
                    c = self.f(iN, jN)
                if c > 0:
                    self.board[iN][jN] = str(c)
                jN = jN + 1
            iN = iN + 1
            jN = 0

tB = GameBoard()
tB.mark_adjacent()
tB.print_board()
