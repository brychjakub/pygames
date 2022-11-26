# Setup Python ----------------------------------------------- #
import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

# make sure you provide your own image
img = pygame.transform.scale((pygame.image.load('spaceship_red.png').convert()),(80,80))
img.set_colorkey((0,0,0))

angle = 0
running = True
# Loop ------------------------------------------------------- #
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    keys = pygame.key.get_pressed()
    screen.fill((0,50,0))

    if keys[K_w]:
        angle += 6
        
        # Background --------------------------------------------- #

        mx, my = 250,250
        img_copy = pygame.transform.rotate(img, angle)
        screen.blit(img_copy, (mx - int(img_copy.get_width() / 2), my - int(img_copy.get_height() / 2)))
        
    # Buttons ------------------------------------------------ #
    
                
    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)