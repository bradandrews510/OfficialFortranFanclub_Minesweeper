"""
Cell Grid, New game, help, quit buttons functionality

"""
import pygame


class button(pygame.sprite.Sprite):
	"""
	define button object 
	"""

	cell_image = pygame.image.load('cell_image.png')
	def __init__(self, x_start,y_start,width, height):
		"""
		Constructor taking beginning x and y pos, and width/height
		"""
		#
		super().__init__()

def button(msg, x_pos, y_pos, width, height, color, action = None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	print(click)
	if x_pos+width > mouse[0] > x_pos and y_pos+height > mouse[1] > y_pos:
		if(click[0] == 1 and action != None):
			action()

def quit_game():
	pygame.quit()
	quit()

#def help():
	

class minesweeper_gui:

	def gui_start(self,rows,cols,mines):
		pygame.init()
		

		cell_size = 20
		black = (0,0,0)
		white = (255,255,255)
		gray = (128,128,128)
		cell_image = pygame.image.load('cell_image.png')
		gameDisplay = pygame.display.set_mode((display_width, display_height))		

		
		#loop through rows
		for row in range(rows):
			#loop through each column
			for column in range(cols):
				#draw resource at position
				#pygame.draw.rect(gameDisplay,gray, (column*cell_size, row*cell_size,cell_size,cell_size))
				gameDisplay.blit(cell_image, (row * cell_size, 40 + column * cell_size))
		
		pygame.display.set_caption('Minesweeper')
		running = True
		while(running):
			for event in pygame.event.get():
				print(event)
				if event.type == pygame.QUIT:
					running = False
				#if event.type == pygame.MOUSEBUTTONDOWN:
					#mouse_pos = event.pos
					#if button.
			pygame.display.update()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
ms = minesweeper_gui()
ms.gui_start(10,10,0)
