
#executive to run minesweeper

import pygame
from newgame import new_game

class executive:
    # board = 0
    #
    # def __init__(self):
    #     board = 1

    def run(self):
        rows = int(input("How many rows? "))
        cols = int(input("How many columns? "))
        mines = int(input("How many mines? "))
        game = new_game(rows, cols, mines)
        game.start_game()

exec = executive()
exec.run()
