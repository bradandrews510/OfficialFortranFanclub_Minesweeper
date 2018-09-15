# Game logic

# Win
'''
    if(count == remaining):
        print("WIN GAME STUFF HERE")
        pygame.quit()
        sys.exit()


        if(mine_hit):
            #mine_hit = False
            print("THE NEW GAME WAS Not PRESSED YET----------")
            game_over(gameDisplay)
            print("THE NEW GAME WAS PRESSED----------")

    def reveal(gB, row,col):
        return recReveal(gB,row,col)
'''

# Lose

'''def board_create(grid):
    #print(grid.get_height(), " by ", grid.get_width())
    for rows in range(grid.get_height()):
        for cols in range(grid.get_width()):
            #print(rows, ":", cols)
            if grid.board[rows][cols].textRep=='M':
                adjacent(grid, rows-1, cols-1)
                adjacent(grid, rows-1, cols)
                adjacent(grid, rows-1, cols+1)
                adjacent(grid, rows, cols+1)
                adjacent(grid, rows+1, cols+1)
                adjacent(grid, rows+1, cols)
                adjacent(grid, rows+1, cols-1)
                adjacent(grid, rows, cols-1)

    grid.print_board()'''


# Populate the game board with mines
def place_mines(grid, numofMines):
    """ @pre    The number of mines n is valid
        @post   Populates the grid with n mines
        @return None
    """

    mCounter = numofMines

    while mCounter > 0:
        i = random.randint(0, grid.height - 1)
        j = random.randint(0, grid.width  - 1)

        if grid.board[i][j].isMined == False:
            grid.board[i][j].set_mine()
            mCounter = mCounter - 1
