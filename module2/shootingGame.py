import pygame

pygame.init()

screen= pygame.display.set_mode(800,600)
pygame.display.set_caption('Shooter Game')

class Player():
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(50,30)
        self.imgae.fill(0,0,255)
        self.rect = self.image.get_rect()
        self.rect.center = ()






running = True

while running:
 for event in pygame.event.get():
      if event.type == pygame.quit:
         running = False

pygame.quit()