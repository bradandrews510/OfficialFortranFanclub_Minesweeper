"""@package docstring
   Executive - will run the minesweeper game
"""

import pygame
from sweeper_UI import *

class executive:

    def run(self):
        """
        @pre none
        @post runs a game
        """
        print("WELCOME TO MINESWEEPER!")


        while True:

            self.get_input()
            start_game(self.rows, self.cols, self.mines)


    def get_input(self):
        """
        @pre none
        @post sets rows, columns and mines equal to a valid user input (2 <= rows <= 30, 2 <= cols <= 40, 1 <= mines <= rows*cols -1)
        """
        while True:
            try:
                self.rows = int(input("Number of rows: "))
                while self.rows < 2 or self.rows > 30:
                    self.rows = int(input("Please enter a number between 2 and 30: "))
                break
            except ValueError:
                print("Please enter a number!")

        while True:
            try:
                self.cols = int(input("Number of columns: "))
                while self.cols < 2 or self.cols > 40:
                    self.cols = int(input("Please enter a number between 2 and 40: "))
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
