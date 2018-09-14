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

        # This is the text representation of what's in the cell
        # M: Mine
        # n: The number of adjacent mines. Can only occurs when isMined == False
        self.textRep = '-'

    def set_mine(self):
        self.isMined = True
        self.textRep = 'M'

    # Toggle the isFlagged flag
    """ @post   Toggles the isFlagged state
        @return 0 indicates nothing was done, -1 means the cell was unflagged,
                and 1 means that the cell was flaggeds
    """
    def set_flag(self):
        if self.isRevealed == True:
            return 0

        if self.isFlagged == False:
            self.isFlagged = True
            return -1 # This is supposed to subtract one flag from the player's
            # available flags

        elif self.isFlagged == True:
            self.isFlagged = False
            return 1 # Return +1 flags to player

        else:
            print("Error, we should not have reached this point")

    # Once revealed, a mine cannot be unrevealed
    def set_revealed(self):
        self.isRevealed = True

    # Set the number of adjacent mines to nMines
    def set_num_adj_mines(self, nMines):
        # We convert the number of mines to a string in order to keep all text
        # representations as the same data type
        self.numAdjacent = str(nMines)

    def get_cell_textRep(self):
        return self.textRep
