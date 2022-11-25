import pygame, random

pygame.init()


WINDOW_WIDTH = 800
WINDO_HEIGTH = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDO_HEIGTH))
pygame.display.set_caption(" sprite groups ")


FPS = 60
clock = pygame.time.Clock()

#define classes
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("blue_monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.velocity = random.randint(1, 10)
    
    def update(self):       #musí být pojmenované upate, jinak nejede(je to Sprite funkce)
            #update to move the monsters
        self.rect.y += self.velocity
        

#create a monster group and creat 10 monsters
monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster((random.randint(0, 800)),(random.randint(0, 800)))
    monster_group.add(monster) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill the display
    display_surface.fill((0,0,0))

    #update and blit assets
    #monster_group.update()
    monster_group.draw(display_surface)


    pygame.display.update()
    clock.tick(FPS)


pygame.quit()