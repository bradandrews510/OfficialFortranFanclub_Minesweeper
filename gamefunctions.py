import pygame, sys, time, random
from pygame.locals import *

'''pygame.init()

(width,height) = (300,200)
screen = pygame.display.set_mode((width,height))
pygame.display.flip()

while(true)'''


def recReveal(grid, rows, cols):

    if rows>=grid.get_height() or rows<0 or cols>=grid.get_width() or cols<0 or grid[rows][cols].get_revealed()==True:
        return

    grid.board[rows][cols].set_revealed()


    if grid.board[rows][cols]=='M':
        print("game over")

    elif grid.board[rows][cols]!='-':
        print("Stop point- ", rows, ":", cols, ":", grid.board[rows][cols])

    elif grid.board[rows][cols]=='-':
        print(rows, ":", cols, ":", grid.board[rows][cols])
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
    for row in grid:
        for col in grid[row]:
            if grid[row][col].textRep=='M':
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
    if rows>=grid.get_height() or rows<0 or cols>=grid.get_width() or cols<0 or grid.board[rows][cols].get_revealed()==True:
        return

    grid[rows][cols].set_num_adj_mines(grid[rows][cols].get_num_adj_mines()+1)
    grid[rows][cols].set_text_rep(grid[rows][cols].get_num_adj_mines())
    return
