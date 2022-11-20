import pygame
pygame.init()


WINDOW_WIDTH = 600
WINDOWN_HEIGTH = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOWN_HEIGTH))
pygame.display.set_caption("blitting images")


#create imagex .... returns a surface objcect with the image drawn on it
dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()     #get_rect() vytvoří automaticky rect okolo obrázku
dragon_left_rect.topleft = (0,0)

dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #blit (copy) a surface object at the given coordinates to our display
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    pygame.draw.line(display_surface, (255,255,255), (0,64), (WINDOW_WIDTH,64), 5)
    
   
    #update the display
    pygame.display.update()

pygame.quit()