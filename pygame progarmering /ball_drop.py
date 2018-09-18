import pygame
import math
from random import randint

screen_width = 1000
screen_hight = 1000
height = randint(1,100)
x_ball =490-height*9


Rundetaarn = pygame.image.load("rundetaarn(1).png")
screen = pygame.display.set_mode((screen_width,screen_hight))
pygame.display.init()
pygame.init()
screen.fill([255,255,255])

def message_display(text):
    font = pygame.font.Font("Crimson-Roman.ttf",20)
    text_surf = font.render(text,True,([0,0,0]))
    screen.blit(text_surf,[10,10])

def ball_drop_physics():
    print("A ball is thrown out of a tower at the height of ",height,"meters")

    guess = float(input("How long du you think it takes the ball to reach the ground?: "))

    time = math.sqrt((-height)/(1/2*(-9.82)))
    print ("\nThe ball hits the ground after ",time, " seconds")

    deviation = abs(time - guess)
    print("\nYou were off by ",deviation," seconds")

    deviation_percentage = int((abs(time - guess) / time) *100)
    print("You'r deviation in percentage is",deviation_percentage,"%")

    if deviation_percentage < 10:
        print("Very good")

def gameloop():
    run = True
    while run:
        pygame.time.delay(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            
        #message_display("En bold bliver smidt ud fra Rundetårn i en højde af ")
        pygame.draw.circle(screen,(0, 64, 64, 64),(70,x_ball),10,10)
        screen.blit(Rundetaarn, (100,100))
        pygame.display.update()
    pygame.quit()
print(height)
print(x_ball)
gameloop()


