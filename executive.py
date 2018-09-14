
#executive to run minesweeper

import pygame
from newgame import new_game

class executive:
    # board = 0
    #
    # def __init__(self):
    #     board = 1

    def run(self):
        print("WELCOME TO MINESWEEPER!")
        rows = int(input("Number of rows: "))
        cols = int(input("Number of columns: "))
        mines = int(input("Number of mines: "))
        #add checks for valid input
        game = new_game(rows, cols, mines)
        game.start_game()

exec = executive()
exec.run()
