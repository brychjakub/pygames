import pygame

pygame.init()


WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

display = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("adding sounds")

#load sound effects
sound_1 = pygame.mixer.Sound('sound_1.wav')
sound_2 = pygame.mixer.Sound('sound_2.wav')

#play the sound effects
sound_1.play()
pygame.time.delay(2000)     #waiting a little before second sounds  
sound_2.play()
pygame.time.delay(2000)

#change volume of the sound effect
sound_2.set_volume(.1)
sound_2.play()

#load background music
pygame.mixer.music.load('music.wav')

#play and stop the music
pygame.mixer.music.play(-1, 0.0)    #(numberOfTimes, StartingTime)--> -1 for infinite loop
pygame.time.delay(1000)
sound_1.play(1)     #playing while background music, (1) for repeating it once
pygame.time.delay(5000)
pygame.mixer.music.stop()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
