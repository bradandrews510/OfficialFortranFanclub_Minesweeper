
#executive to run self.minesweeper

import pygame
from newgame import new_game

class executive:
    # board = 0
    #
    # def __init__(self):
    #     board = 1

    def run(self):
        print("WELCOME TO MINESWEEPER!")

        self.get_input()

        #self.mines = int(input("Number of mines: "))
        #add checks for valid input
        game = new_game(self.rows, self.cols, self.mines)
        game.start_game()
        game.run_game()

    def get_input(self):
        while True:
            try:
                self.rows = int(input("Number of rows: "))
                while self.rows < 2:
                    self.rows = int(input("Please enter a number greater than 1: "))
                break
            except ValueError:
                print("Please enter a number!")

        while True:
            try:
                self.cols = int(input("Number of columns: "))
                while self.cols < 2:
                    self.cols = int(input("Please enter a number greater than 1: "))
                break
            except ValueError:
                print("Please enter a number!")

        while True:
            try:
                self.mines = int(input("Number of mines: "))
                while self.mines < 1 or (self.mines >= self.rows * self.cols):
                    tile_count = self.rows * self.cols
                    self.mines = int(input("Please enter a number between 1 and " + str(tile_count - 1) + ": "))
                break
            except ValueError:
                print("Please enter a number!")


exec = executive()
exec.run()
