
#executive to run self.minesweeper

import pygame
from UI import *

'''
def run(self):
    print("WELCOME TO MINESWEEPER!")
    while True:
        self.get_input()
        start_game(self.rows, self.cols, self.mines)

def get_input(self):
    try:
        self.rows = int(input("Number of rows: "))
        while self.rows < 2 or self.rows > 30:
            self.rows = int(input("Please enter a number between 2 and 30: "))
        break
    except ValueError:
        print("Please enter a number!")

    try:
        self.cols = int(input("Number of columns: "))
        while self.cols < 2 or self.cols > 40:
            self.cols = int(input("Please enter a number between 2 and 40: "))

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
'''

def get_row_count():
    rows = int( input("Enter the number of rows: ") )
    # Check for errors

def get_column_count():
    columns = int( input("Enter the number of columns: ") )
    # Check for errors

def get_number_of_mines():
    mines = int( input("Enter the number of mines: ") )
