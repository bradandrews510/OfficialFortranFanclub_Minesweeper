
#executive to run self.minesweeper

import pygame
from newgame import new_game
from sweeper_UI import minesweeper_gui

class executive:

    def run(self):
        print("WELCOME TO MINESWEEPER!")

        self.get_input()

        #self.mines = int(input("Number of mines: "))
        #add checks for valid input
        # game = new_game(self.rows, self.cols, self.mines)
        # game.start_game()
        # game.run_game()
        ms = minesweeper_gui()
        ms.gui_start(self.rows, self.cols, self.mines)

    def get_input(self):
        while True:
            try:
                self.rows = int(input("Number of rows: "))
                while self.rows < 2 or self.rows > 31:
                    self.rows = int(input("Please enter a number between 2 and 30: "))
                break
            except ValueError:
                print("Please enter a number!")

        while True:
            try:
                self.cols = int(input("Number of columns: "))
                while self.cols < 2 or self.cols > 21:
                    self.cols = int(input("Please enter a number between 2 and 20: "))
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
