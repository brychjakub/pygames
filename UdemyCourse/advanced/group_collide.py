import pygame, random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(" group collide ")


FPS = 60
clock = pygame.time.Clock()

class Game():
    def __init__(self, monster_group, knight_group):
        self.monster_group = monster_group
        self.knight_group = knight_group

    def update(self):
        self.check_collisions()     #tady bych klidně mohl mít JEN check_collisions(), ale update() se hodí na víc věcí, vložim tam fce a pak zavolám jenom update()

    def check_collisions(self):
        """tady coliduju dvě grupy, v závorce true pro zničení 1. grupy (monsters), False pro nezničení 2. groupy"""
        pygame.sprite.groupcollide(self.monster_group, self.knight_group, True, False)  



class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.velocity = random.randint(1, 5)
    
    def update(self):   
        self.rect.y -= self.velocity

   
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("blue_monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.velocity = random.randint(1, 5)
    
    def update(self):       
        self.rect.y += self.velocity

my_monster_group = pygame.sprite.Group()
for i in range(12):
    monster = Monster(i*64, 10)
    my_monster_group.add(monster)

my_knight_group = pygame.sprite.Group()
for i in range(12):
    knight = Knight(i*64, WINDOW_HEIGHT-64)  
    my_knight_group.add(knight)   

my_game = Game(my_monster_group,my_knight_group)        #pokud tady mám groupy, musím je passnout do classy


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill((0,0,0,))

    my_monster_group.update()
    my_monster_group.draw(display_surface)
    my_knight_group.update()
    my_knight_group.draw(display_surface)


    my_game.update()
        #Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()