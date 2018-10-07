import pygame
import tkinter as tk
import random
from random import shuffle
from tkinter import messagebox
from tkinter import*
from tkinter import ttk


class matchgui:
    def __init__(self, parent):
        self.parent = parent
        self.buttons = [[tk.Button(root, font=14, width=4, height=2, command=lambda row=row, column=column:
        self.select(row, column) ) for column in range(4)] for row in range(2)]
        for row in range(2):
            for column in range(4):
                self.buttons[row][column].grid(row=row, column=column)

        self.state = False
        self.setupboard()

    def setupboard(self):
        self.board = list('AABBCCDD')
        random.shuffle(self.board)
        self.board = [self.board[:4], self.board[4:8]]
        for row in self.buttons:
            for button in row:
                button.config(text='', state=tk.NORMAL)

    def select(self, row, column):
        self.buttons[row][column].config(text=self.board[row][column])
        self.buttons[row][column].config(state=tk.DISABLED)
        if not self.state:
            self.state = (row, column)
        else:
            a,b = self.state
            if self.board[row][column] == self.board[a][b]:
                self.board[row][column] = ''
                self.board[a][b] = ''
                if not any(''.join(row) for row in self.board):
                    messagebox.showinfo(title='Success!', message='You win! ')
                    self.parent.after(300, self.setupboard)
            else:
                self.parent.after(300, self.cover, row, column, a, b)
            self.state = False

    def cover(self, x1, y1, x2, y2):
        self.buttons[x1][y1].config(text='', state=tk.NORMAL)
        self.buttons[x2][y2].config(text='', state=tk.NORMAL)



root = tk.Tk()
matchgui(root)
root.title("Matching game!")
"""photo = PhotoImage(file="apple.png")
label1 = Label1(root,image=photo)
label1.pack()"""
"""label = tk.Label(root, text="Welcome to the matching game!")"""
"""button = tk.Button(root, text="Start")"""
"""label.grid(column=0,row=0)"""
"""button.grid(column=1,row=0)"""
root.mainloop()
