import pygame
import math
from random import randint
from pygame.locals import *

screen_width = 1000
screen_hight = 1000
height = randint(1,42)

x_ball =490-height*9


Rundetaarn = pygame.image.load("/Users/louis/Documents/GitHub/Programmering--spil/pygame progarmering /rundetaarn(1).png")
screen = pygame.display.set_mode((screen_width,screen_hight))
pygame.display.init()
pygame.init()
screen.fill([255,255,255])
font = pygame.font.SysFont("Times New Roman",20)
keys = pygame.key.get_pressed()
movex = 0 

def message_display(text,x_text,y_text):
    text_surf = font.render(text,True,([0,0,0]))
    screen.blit(text_surf,[x_text,y_text])

def render_loop():
    message_display("A ball is thrown out of a tower at the height of ",10,10)
    message_display(str(height),395,10)
    message_display("meters",420,10)
    message_display("How long du you think it takes the ball to reach the ground?: ",10,30)
    pygame.draw.circle(screen,(0, 64, 64, 64),(70,x_ball),10,10)
    screen.blit(Rundetaarn, (100,100))
    pygame.display.update()



def gameloop():
    numX = 510
    numY = 30
    move = 10
    guess = ""
    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

            if (event.type==pygame.KEYDOWN):
                if (event.key==pygame.K_1):
                    guess += "1"
                if (event.key==pygame.K_2):
                    guess += "2"
                if (event.key==pygame.K_3):
                    guess += "3"
                if (event.key==pygame.K_4):
                    guess += "4"
                if (event.key==pygame.K_5):
                    guess += "5"
                if (event.key==pygame.K_6):
                    guess += "6"
                if (event.key==pygame.K_7):
                    guess += "7"
                if (event.key==pygame.K_8):
                    guess += "8"
                if (event.key==pygame.K_9):
                    guess += "9"
                if (event.key==pygame.K_0):
                    guess += "0"
                if (event.key==pygame.K_BACKSPACE):
                    screen.fill([255,255,255])
                    guess = ""
                if (event.key==pygame.K_COMMA):
                    guess += "."
                if (event.key==pygame.K_RETURN):
                    time = math.sqrt((-height)/(1/2*(-9.82)))
                    time = round(time,2)
                    message_display("The ball hits the ground after ",300,100)
                    print(guess)
                    deviation = abs(time - float(guess))
                    deviation = round(deviation,2)
                    message_display(str(time),540,100)
                    message_display(" seconds",580,100)
                    message_display("You were off by",300,120)
                    message_display(str(deviation),440,120)
                    message_display(" seconds",480,120)
                    deviation_percentage = int((abs(time - float(guess)) / time) *100)
                    str(deviation_percentage)
                    message_display("You'r deviation in percentage is",300,140)
                    message_display(str(deviation_percentage),560,140)
                    message_display("%",580,140)
                    if deviation_percentage < 10:
                        message_display("Very good",300,160)
                    #for i in range(height):
                        #global x_ball
                        #x_ball += 9
                        #pygame.draw.circle(screen,(0, 64, 64, 64),(70,x_ball),10,10)
                        #screen.fill([255,255,255])

        render_loop()
        message_display(str(guess),numX,numY)
        #print(movex)

    pygame.quit()
print(height)
print(x_ball)
gameloop()



