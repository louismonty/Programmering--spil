import pygame
import math
from random import randint

screen_width = 1000
screen_hight = 1000
højde = randint(1,42)
x_ball = højde*9 + 100

Rundetaarn = pygame.image.load("rundetaarn(1).png")
screen = pygame.display.set_mode((screen_width,screen_hight))
pygame.display.init()
pygame.init()
screen.fill([255,255,255])

def message_display(text):
    font = pygame.font.Font("Crimson-Roman.ttf",20)
    text_surf = font.render(text,True,([0,0,0]))
    screen.blit(text_surf,[10,10])

def gamestart():
    text1 = ("En bold bliver smidt ud fra Rundetårn i en højde af ",højde,"Meter")

def gameend():
    tid_gæt = float(input("Hvor lang tid tror du det tager i sekunder?: "))

    tid = math.sqrt((-højde)/(1/2*(-9.82)))
    print ("\nBolden rammer jorden efter ",tid, " sekunder")

    afvigelse = abs(tid-tid_gæt)
    print("\nDu gættede forkert med ",afvigelse," sekunder")

    procentvis_afvigelse = int((abs(tid - tid_gæt) / tid) *100)
    print("Din procentvise afvigelse var",procentvis_afvigelse,"%")

def gameloop():
    run = True
    while run:
        pygame.time.delay(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            
        message_display("En bold bliver smidt ud fra Rundetårn i en højde af ")
        pygame.draw.circle(screen,(0, 64, 64, 64),(70,x_ball),20,20)
        screen.blit(Rundetaarn, (100,100))
        pygame.display.update()
    pygame.quit()
print(højde)
print(x_ball)
gameloop()


