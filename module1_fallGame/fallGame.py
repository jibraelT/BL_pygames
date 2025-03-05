import pygame
import random

# Initilaze game -tells computer that the following
#code should be interpretted as a game
pygame.init()

# step 1 step up display
height = 1000
width  = 1200

# this is reusable code thatt represents our game screen.
screen = pygame.display.set_mode((width,height))

# this will allow us to show the title of the game when a
#user opens our game
pygame.display.set_caption("avoid the falling object")

# set frame rate
clock = pygame.time.clock()
FPS = 60

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
class Player:
    def __init__(self):
     self.x = width // 2
     self.y = height - 60
     self.playerwidth= 50
     self.playerheight= 50
     self.playerspeed = 5

    def move(self,keys):
       if keys[pygame. K_LEFT] and self .x > 0:
          self.x = self.playerspeed
       if keys[pygame.K_RIGHT] and self.x < width - self.playewWidth:
              self.x += self.playerspeed
