import pygame
import random
import os

pygame.init()
screen_height = 1000
screen_width = 1000

win = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Platformer")

#define game variables
tile_size = 50    #Tile_size are based on width

#load image
sky = pygame.image.load(os.path.join("pic", "sky.jpeg"))
BG = pygame.transform.scale(sky, (screen_width,screen_height))

def draw_grid():
 for line in range(0,20):     #If you want to make a 5*5 grid, the range should at least be (0,5)
  pygame.draw.line(win, (255,255,255), (0,line*tile_size),(screen_width,line*tile_size))     # the starting and the ending position of line 21 and 22 should be reversed
  pygame.draw.line(win, (255, 255, 255), (line * tile_size ,0), ( line * tile_size ,screen_height))

class World():  #This class is to load the dirt image with the dirt_position chart named "world_data"
 def __init__(self, data):
  self.tile_list = []

  #load the image
  dirt = pygame.image.load(os.path.join("pic", "dirt.jpg"))
  grass = pygame.image.load(os.path.join("pic", "grass.png"))

  row_count = 0 #init row count here
  for row in data:
   col_count = 0   #init col_count here
   for tile in row:
    if tile == 1:
     img = pygame.transform.scale(dirt,(tile_size,tile_size)) #img_rect converts the dirt image from square to rectangle and make them stretch or shrink
     img_rect = img.get_rect()                                 #based on the 1's and 0s on the chart
     img_rect.x = col_count * tile_size                        # The x-cord is going to increase with the col_count
     img_rect.y = row_count *tile_size                         # The Y-cord increases with the row_count
     tile = (img, img_rect)                                    # This "tile" variable stores the img and the coordinate of the image in the list
     self.tile_list.append(tile)                               # Appends the tile to the list and store it

     if tile == 2:
      img = pygame.transform.scale(grass, (tile_size, tile_size))  # img_rect converts the dirt image from square to rectangle and make them stretch or shrink
      img_rect = img.get_rect()  # based on the 1's and 0s on the chart
      img_rect.x = col_count * tile_size  # The x-cord is going to increase with the col_count
      img_rect.y = row_count * tile_size  # The Y-cord increases with the row_count
      tile = (img, img_rect)  # This "tile" variable stores the img and the coordinate of the image in the list
      self.tile_list.append(tile)  # Appends the tile to the list and store it
    col_count += 1                                             #col_count make sure the python is going through the list horizontally.
   row_count += 1                                              # Then row_count is making  sure the program goes to the next row (vertically)

 # NOTE: The "world data" list is an initial list that's not that useful. Therefore, we need this new tile_list to store the useful data ("1s") and use them later
 #Going through the list to draw the dirt accordingly.
 def draw(self):
  for tile in self.tile_list:
   win.blit(tile[0],tile[1])



world_data =[       #position of dirts on the screen, representing the 5 rows and columns drew from the draw grid function
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
 [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
 [1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
 [1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
 [1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

world = World(world_data)

#Game Loop
run = True
while run:
 win.blit(BG, (0, 0))

 world.draw()
 draw_grid()

 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   run = False


 pygame.display.update()
pygame.quit()