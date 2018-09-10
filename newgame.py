import pygame
#from sweeper_UI import ms_buttons
#from Board.py import GameBoard

# drawing background gameboard
# start_game_input(rows, cols, mines) - rows, cols, #mines,
    #create_board()
#newgame()
    # createnew()
        #drawcells(rows, cols)
    # create number_and_mine_grid()

class new_game:
    m_rows = 0
    m_cols = 0
    m_mines = 0
    #m_board = GameBoard(rows, cols, mines)

    def __init__(rows, cols, mines):
        start_game_input(rows, cols, mines)

    def start_game_input(rows, cols, mines):
        m_rows = rows
        m_cols = cols
        m_mines = mines
        #m_board = GameBoard(rows, cols, mines)

    def start_game():
        #create window, draw cells, create number and mine grid
        pygame.init()

        pygame.display.set_caption("MINESWEEPER")

        screen = pygame.display.set_mode((240,180))

        running = true

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = false
