"""@package docstring
   Cell class?
"""

class Cell:
    def __init__(self):
        # The default cell is completely blank
        self.isMined     = False
        self.isFlagged   = False
        self.isRevealed  = False
        self.numAdjacent = 0

        self.textRep = '-'

    def set_mine(self):
        self.isMined = True
        self.textRep = 'M'

    # Toggle the isFlagged flag
    def set_flag(self):
        self.isFlagged = not(self.isFlagged)

    # Once revealed, a mine cannot be unrevealed
    def set_revealed(self):
        self.isRevealed = True

    # Set the number of adjacent mines to nMines
    def set_num_adj_mines(self, nMines):
        self.numAdjacent = nMines

    def get_cell_textRep(self):
        return self.textRep



#tC = Cell()
