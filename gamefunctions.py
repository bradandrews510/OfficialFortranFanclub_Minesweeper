#import pygame, sys, time, random
#from pygame.locals import *

from Cell import *
from Board import *

'''pygame.init()

(width,height) = (300,200)
screen = pygame.display.set_mode((width,height))
pygame.display.flip()

while(true)'''


def recReveal(grid, rows, cols):

    if rows>=grid.get_height() or rows<0 or cols>=grid.get_width() or cols<0 or grid.board[rows][cols].isRevealed==True:
        return

    grid.board[rows][cols].set_revealed()


    if grid.board[rows][cols].get_cell_textRep()=='M':
        print("game over")

    elif grid.board[rows][cols].get_cell_textRep()!='-':
        print("Stop point- ", rows, ":", cols, ":", grid.board[rows][cols].get_cell_textRep())

    elif grid.board[rows][cols].get_cell_textRep()=='-':
        print(rows, ":", cols, ":", grid.board[rows][cols].get_cell_textRep())
        recReveal(grid, rows-1, cols-1)
        recReveal(grid, rows-1, cols)
        recReveal(grid, rows-1, cols+1)
        recReveal(grid, rows, cols+1)
        recReveal(grid, rows+1, cols+1)
        recReveal(grid, rows+1, cols)
        recReveal(grid, rows+1, cols-1)
        recReveal(grid, rows, cols-1)

    return

def board_create(grid):
    #print(grid.get_height(), " by ", grid.get_width())
    for rows in range(grid.get_height()):
        for cols in range(grid.get_width()):
            #print(rows, ":", cols)
            if grid.board[rows][cols].textRep=='M':
                adjacent(grid, rows-1, cols-1)
                adjacent(grid, rows-1, cols)
                adjacent(grid, rows-1, cols+1)
                adjacent(grid, rows, cols+1)
                adjacent(grid, rows+1, cols+1)
                adjacent(grid, rows+1, cols)
                adjacent(grid, rows+1, cols-1)
                adjacent(grid, rows, cols-1)

    return

def adjacent(grid, rows, cols):
    if rows>=grid.get_height() or rows<0 or cols>=grid.get_width() or cols<0 or grid.board[rows][cols].isRevealed==True:
        return

    grid.board[rows][cols].set_num_adj_mines(int(grid.board[rows][cols].numAdjacent)+1)
    grid.board[rows][cols].textRep=grid.board[rows][cols].numAdjacent
    return

print("2x2 with 2 mines")
tB = Board(50,50,50)
board_create(tB)
tB.print_board()
recReveal(tB, 0, 0)
