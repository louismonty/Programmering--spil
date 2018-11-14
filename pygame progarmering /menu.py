import pygame

screen_width = 1000
screen_hight = 1000

screen = pygame.display.set_mode((screen_width,screen_hight))
pygame.display.init()
pygame.init()
screen.fill([255,255,255])
run = True
while run:
    for event in pygame.event.get:
        if event.type == pygame.quit:
            pygame.Rect(500, 508, 214, 43)
            run=False



pygame.quit()