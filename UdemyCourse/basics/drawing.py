import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("drawing objects")



BLACK = (0,0,0,)
WHITE = (255,255,255)
MY_GREEN = (80,150,75)
GREEN = (0,255,0)
BLUE = (0,0,255)


display_surface.fill(MY_GREEN)


#LINE(surface, color, starting point, ending point, whickness)
pygame.draw.line(display_surface, BLACK, (0,0), (100,100),5)


#rectangle(surface, color, (top-left x, top-left y, width, height))
pygame.draw.rect(display_surface, BLUE, (500, 0, 100, 100))
 


#CIRCLE(surface, color, center, radius, thickness....0 for filling the circle)
pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 200, 6)
pygame.draw.circle(display_surface, BLACK, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 194, 110)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    pygame.display.update()



pygame.quit()