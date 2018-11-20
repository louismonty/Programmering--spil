import pygame
import math
from random import randint
from pygame.locals import *

#Definitons
screen_width = 1000
screen_hight = 1000
#Radom height
height = randint(1,42)
#Ball heigt in pixels
x_ball =490-height*9
Rundetaarn = pygame.image.load("/Users/louis/Documents/GitHub/Programmering--spil/pygame progarmering /rundetaarn(1).png")
screen = pygame.display.set_mode((screen_width,screen_hight))
#Initialize screen
pygame.display.init()
pygame.init()
#Make screen white
screen.fill([255,255,255])
#Font for tekst
font = pygame.font.SysFont("Times New Roman",20)


#Text editor
def message_display(text,x_text,y_text):
    text_surf = font.render(text,True,([0,0,0]))
    screen.blit(text_surf,[x_text,y_text])

#render loop
def render_loop():
    #Tekst to render 
    message_display("A ball is thrown out of a tower at the height of ",10,10)
    message_display(str(height),395,10)
    message_display("meters",420,10)
    message_display("How long du you think it takes the ball to reach the ground?: ",10,30)
    #Draws cirkel at tower
    pygame.draw.circle(screen,(0, 64, 64, 64),(70,x_ball),10,10)
    #Draws tower
    screen.blit(Rundetaarn, (100,100))
    #Updates display 
    pygame.display.update()


#Gameloop
def gameloop_bd():
    #Definition
    #Clean guess
    guess = ""
    run = True
    while run:
        #Makes game run in loop 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            #Checks if a button is pressed
            if (event.type==pygame.KEYDOWN):
                #Checks if 1 key is pressed
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
                #Deletes the texst 
                if (event.key==pygame.K_BACKSPACE):
                    screen.fill([255,255,255])
                    guess = ""
                #Write a comma  
                if (event.key==pygame.K_COMMA):
                    guess += "."
                #Checks if enter key is pressed
                if (event.key==pygame.K_RETURN):
                    #calculates the answer
                    time = math.sqrt((-height)/(1/2*(-9.82)))
                    time = round(time,2)
                    message_display("The ball hits the ground after ",300,100)
                    #calculates the deviation
                    deviation = abs(time - float(guess))
                    deviation = round(deviation,2)
                    message_display(str(time),540,100)
                    message_display(" seconds",580,100)
                    message_display("You were off by",300,120)
                    message_display(str(deviation),440,120)
                    message_display(" seconds",480,120)
                    #calculates the deviation precentage 
                    deviation_percentage = int((abs(time - float(guess)) / time) *100)
                    str(deviation_percentage)
                    message_display("You'r deviation in percentage is",300,140)
                    message_display(str(deviation_percentage),560,140)
                    message_display("%",580,140)
                    #if the guess is within 10%
                    if deviation_percentage < 10:
                        message_display("Very good",300,160)


        render_loop()
        message_display(str(guess),510,30)
#gameloop_bd()
pygame.quit()



