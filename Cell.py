"""@package docstring
   Cell.py contains the cell class that will populate the game board. Cell()
   objects contain both get and set functions because they change state both
   as a result of direct and indirect player actions. That is, an adjacent cells
   can affect each other even if the player only clicks on one.
"""

class Cell:
    def __init__(self):
        """ @pre    By default, the cell class does not assume anything
        and upon initialization is completely blank
            @post   Nothing is done upon initialization
        """
        # The default cell is completely blank
        self.isMined     = False
        self.isFlagged   = False
        self.isRevealed  = False
        self.numAdjacent = 0

        # This is the text representation of what's in the cell. It's used to
        # tell the renderer what to draw. The renderer must decide what to draw
        # based on the revealed status of the cell though
        # M: Mine
        # n: The number of adjacent mines. Can only occurs when isMined == False
        self.textRep = '-'

    def set_mine(self):
        """ @pre    There is no sanity or error checking of any kind here, so
        it's assumed that it is only called when necessary
            @post   Enables the cell's mine and updates it's text representation
        """
        self.isMined = True
        self.textRep = 'M'

    # Toggle the isFlagged flag
    def set_flag(self):
        """ @pre    No error checking is done so it's posible to flag or unflag
        even cells that have already been revealed. It's assumed to only be called
        when necessary
            @post   Toggles the isFlagged state
            @return 0 indicates nothing was done, -1 means the cell was unflagged,
                    and 1 means that the cell was flaggeds
        """
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
        """ @pre    There is no sanity or error checking of any kind here, so
        it's assumed that it is only called when necessary
            @post   Marks a cell as having been revealed
        """
        self.isRevealed = True

    # Set the number of adjacent mines to nMines
    def set_num_adj_mines(self, nMines):
        """ @pre    There is no sanity or error checking of any kind here, so
        it's assumed that only valid data is passed
            @post   Changes the text representation of the cell to match the
        number of adjacent mines
        """
        # We convert the number of mines to a string in order to keep all text
        # representations as the same data type
        self.numAdjacent = str(nMines)

    def get_cell_textRep(self):
        """ @pre    No error checking, it's assumed this the value of textRep
        is valid and returnable
            @return Cell's text representation
        return self.textRep
