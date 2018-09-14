import pygame
from sweeper_UI import minesweeper_gui

ms = minesweeper_gui
get_inp = True
rows = int(input("Rows: "))
cols = int(input("Columns: "))
mines = int(input("Mines: "))
ms.gui_start(rows, cols, mines)
