import tkinter as tk
from tkinter import *
import pygame
from pygame.locals import *
import math
import sys
import os
from tkinter import simpledialog

#This is required before creating the window
#app = Tk()

class ms_buttons:

    def start(self, master):
        """
        @pre Starts main game window, asks for row, column, mines input
        """

        self.frame = tk.Frame(master)
        
        app.lower()
        
        #create GUI buttons
        self.printbutton = Button(self.frame, text="New Game", command = self.newGame)
        self.printbutton.pack(side = LEFT)
        self.quitbutton = Button(self.frame, text = "quit", command = self.frame.quit)
        self.quitbutton.pack(side = LEFT)

        #get user inputs
        rows = tk.simpledialog.askinteger("Welcome to Minesweeper!", "Enter the number of rows", parent = app, minvalue = 2, maxvalue = 100)
        if rows is not None:
            print(rows)

            cols = tk.simpledialog.askinteger("Welcome to Minesweeper!", "Enter the number of columns", parent = app, minvalue = 2, maxvalue = 100)
            if cols is not None:
                print(cols)

                mines = tk.simpledialog.askinteger("Welcome to Minesweeper!", "Enter the number of mines", parent = app, minvalue = 1, maxvalue = rows * cols - 1)
                if mines is not None:
                    print(mines)
                else:
                    self.frame.quit
            else:
                self.frame.quit
        else:
            self.frame.quit

        app.focus_set()
        app.tkraise()
        self.frame.pack()
    


    def newGame(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

"""
construct an ms_buttons object
ms = ms_buttons()

starts running of window
ms.start(app)

keeps game loop running
app.mainloop()
"""
