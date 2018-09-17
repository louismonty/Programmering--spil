import pygame
import math 

screen_width = 1000
screen_hight = 1000

Rundetaarn = pygame.image.load("rundetaarn(1).png")
screen = pygame.display.set_mode((screen_width,screen_hight))
pygame.display.init()

run = True
while run:
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.draw.circle(screen,(0, 64, 64, 64),(90,100),20,20)
    screen.blit(Rundetaarn, (100,100))
    pygame.display.update()
pygame.quit()
