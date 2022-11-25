import pygame, random

pygame.init()


WINDOW_WIDTH = 800
WINDO_HEIGTH = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDO_HEIGTH))
pygame.display.set_caption(" sprite groups ")


FPS = 60
clock = pygame.time.Clock()

#define classes

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, monster_group):
        super().__init__()      #toto zde musí být, inicializuje se tim Sprite class (což je super klasa k našim classam)
        self.image = pygame.image.load("knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.velocity = 5

        self.monster_group = monster_group

    def update(self):
        self.move()
        self.check_collisions()

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocity

    def check_collisions(self):
       """check for collisions between player and monster group"""
       if pygame.sprite.spritecollide(self, monster_group, True):
            print(len(monster_group))


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
my_monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i*64, 10)
    my_monster_group.add(monster) 
        
#create a player group
player_group = pygame.sprite.Group() 
player = Player(500, 500, my_monster_group)
player_group.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill the display
    display_surface.fill((0,0,0))

    #update and blit assets
    player_group.update()
    player_group.draw(display_surface)
    monster_group.update()
    monster_group.draw(display_surface)


    pygame.display.update()
    clock.tick(FPS)


pygame.quit()