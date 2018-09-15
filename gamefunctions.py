from pygame.locals import *

from Board import *


def recReveal(grid, rows, cols):
    if rows>=grid.get_height() or rows<0 or cols>=grid.get_width() or cols<0 or grid.board[rows][cols].isRevealed==True:
        return False

    grid.board[rows][cols].set_revealed()

    if grid.board[rows][cols].get_cell_textRep()=='M':
        print("Stop point- ", rows, ":", cols, ":", grid.board[rows][cols].get_cell_textRep())
        return True

    elif grid.board[rows][cols].get_cell_textRep()!='-':
        print("Stop point- ", rows, ":", cols, ":", grid.board[rows][cols].get_cell_textRep())
        return False

    elif grid.board[rows][cols].get_cell_textRep()=='-':
        print(rows, ":", cols, ":", grid.board[rows][cols].get_cell_textRep())
        recReveal(grid, rows-1, cols-1)
        recReveal(grid, rows-1, cols)
        recReveal(grid, rows-1, cols+1)
        recReveal(grid, rows, cols+1)
        recReveal(grid, rows+1, cols+1)
        recReveal(grid, rows+1, cols)
        recReveal(grid, rows+1, cols-1)
        recReveal(grid, rows, cols-1)

    return False


def adjacent(grid, rows, cols):
    if rows>=grid.get_height() or rows<0 or cols>=grid.get_width() or cols<0 or grid.board[rows][cols].isRevealed==True or grid.board[rows][cols].isMined==True:
        return

    grid.board[rows][cols].set_num_adj_mines(int(grid.board[rows][cols].numAdjacent)+1)
    grid.board[rows][cols].textRep=grid.board[rows][cols].numAdjacent
    return

''' Nathan '''
def game_over(gameSurface):
    print("ENTERED GAME_OVER----------")
    global FPSCLOCK, DISPLAYSURFACE  #Testing purposes
    print("TEST AREA 1----------")

    global BASICFONT, TEXTFONT, RESET_SURF, RESET_RECT, QUIT_SURF, QUIT_RECT
    print("TEST AREA 2----------")

    # pygame.init()  #Testing purposes
    # pygame.display.set_caption('Minesweeper')  #Testing purposes
    FPSCLOCK = pygame.time.Clock()  #Testing purposes
    print("TEST AREA 3----------")
    DISPLAYSURFACE = gameSurface; #Testing purposes
    print("TEST AREA 4----------")
    BASICFONT = pygame.font.SysFont('None', 30)
    print("TEST AREA 5----------")
    TEXTFONT = pygame.font.SysFont('None', 40)
    print("TEST AREA 6----------")
    RESET_SURF, RESET_RECT = drawButton('New Game', (0, 0, 0), (225, 225, 225), 200/3, 100*.75)
    print("TEST AREA 7----------")
    QUIT_SURF, QUIT_RECT = drawButton('Quit', (0, 0, 0), (225, 225, 225), 200*.75, 100*.75)
    print("TEST AREA 8----------")
    MENU_SURF = pygame.Surface((200,100))
    print("TEST AREA 9----------")
    MENU_RECT = placeSurface(MENU_SURF, DISPLAYSURFACE.get_width()/2, DISPLAYSURFACE.get_height()/2)
    print("TEST AREA 10----------")

    RESET_RECT.move_ip(MENU_RECT.left,MENU_RECT.top)
    QUIT_RECT.move_ip(MENU_RECT.left,MENU_RECT.top)

    mouse_x = 0
    mouse_y = 0
    running = True
    print("RUNNING = ", running, "----------")
    #DISPLAYSURFACE.fill((0,0,0))

    while(running):
        mouseClicked = False
        spacePressed = False
        running = True

        #DISPLAYSURFACE.fill((0,0,0))  #Testing purposes

        DISPLAYSURFACE.blit(MENU_SURF, MENU_RECT)
        MENU_SURF.fill((255,255,255))
        drawText("Game Over", TEXTFONT, ((0,0,0)), MENU_SURF, 200*.5, 100*.25)

        DISPLAYSURFACE.blit(RESET_SURF, RESET_RECT)
        DISPLAYSURFACE.blit(QUIT_SURF, QUIT_RECT)



        if RESET_RECT.collidepoint(mouse_x, mouse_y):
            highlightButton(DISPLAYSURFACE, RESET_RECT)
            if mouseClicked:
                running = False
                pygame.quit()
                break

        # check if show box is clicked
        if QUIT_RECT.collidepoint(mouse_x, mouse_y):
            highlightButton(DISPLAYSURFACE, QUIT_RECT)
            if mouseClicked:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(30)


def placeSurface(screen, center_x, center_y):

    surfRect = screen.get_rect()
    surfRect.centerx = center_x
    surfRect.centery = center_y

    return surfRect
