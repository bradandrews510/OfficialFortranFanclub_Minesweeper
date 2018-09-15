'''
cell_list = [[0 for i in range(cols)] for j in range(rows)]
      #loop through rows
  for row in range(rows):
      #loop through each column
  for column in range(cols):
          #pygame.draw.rect(gameDisplay,gray, (column*cell_size, row*cell_size,cell_size,cell_size))
                      cell_list[row][column] = cell_button(column,row,cell_size,cell_size,gB.board[row][column])
                      gameDisplay.blit(cell_image, (column * cell_size, 40 + row * cell_size))



              mine_hit = False

                                  for row in range(rows):
                      for cell in cell_list[row]:
                          if cell.m_cell.isRevealed:
                              count += 1
                              gameDisplay.blit(cell_contents[gB.board[cell.y][cell.x].get_cell_textRep()], (cell.x * cell_size, 40 + cell.y * cell_size))
                          elif cell.m_cell.isFlagged:
                              gameDisplay.blit(flag_image,(cell.x * cell_size, 40 + cell.y * cell_size))
                          else:
                              gameDisplay.blit(cell_image, (cell.x * cell_size, 40 + cell.y * cell_size))



                  pygame.display.update()
'''
