import pygame
import math
import os
from random import randint

screen_width = 1100
screen_hight = 1000
screen = pygame.display.set_mode((screen_width,screen_hight))
pygame.display.init() 
pygame.init()
font = pygame.font.SysFont("Times New Roman",30)
screen.fill([255,255,255])


def message_display(text,x_text,y_text):
    text_surf = font.render(text,True,([0,0,0]))
    screen.blit(text_surf,[x_text,y_text])




def gameloop_ac():
    pygame.init()
    run = True
    geuss = ""
    time = randint(1,20)
    acceleration = ((40/3.6)/time)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

            start_print ="A car is in a race and the green light is turning on, the car reaches 40km/h at "
            start_print += str(time)
            start_print += " seconds"
            message_display(str(start_print),1,1)
            message_display("At which acceleration do you the think the car will gain?: ",1,40)
            if (event.type==pygame.KEYDOWN):
                if (event.key==pygame.K_1):
                    geuss += "1"
                if (event.key==pygame.K_2):
                    geuss += "2"
                if (event.key==pygame.K_3):
                    geuss += "3"
                if (event.key==pygame.K_4):
                    geuss += "4"
                if (event.key==pygame.K_5):
                    geuss += "5"
                if (event.key==pygame.K_6):
                    geuss += "6"
                if (event.key==pygame.K_7):
                    geuss += "7"
                if (event.key==pygame.K_8):
                    geuss += "8"
                if (event.key==pygame.K_9):
                    geuss += "9"
                if (event.key==pygame.K_0):
                    geuss += "0"
                if (event.key==pygame.K_BACKSPACE):
                    screen.fill([255,255,255])
                    geuss = ""
                if (event.key==pygame.K_COMMA):
                    geuss += "."
                if (event.key==pygame.K_RETURN):
                    time = round(time,2)
                    acceleration_print = "Acceleration is "
                    acceleration_print += str(round(acceleration,2))
                    acceleration_print += " m/s^2"
                    message_display(acceleration_print,300,100)
                    deviation_print = "You were off by "
                    deviation_print += str(round(acceleration-float(geuss),2))
                    deviation_print += " m/s^2"
                    message_display(deviation_print,300,130)
                    deviation_percentage = int((abs(acceleration - float(geuss))/time)*100)
                    deviation_percentage_print = "You´r devition in percentage is "
                    deviation_percentage_print += str(deviation_percentage)
                    deviation_percentage_print += "%"
                    message_display(deviation_percentage_print,300,160)

                    #delevation = abs(acceleration - float(geuss))
                    #deviation = round(deviation,2)
                    #message_display(str(time),540,100)
                    #message_display(" seconds",580,100)
                    #message_display("You were off by",300,120)
                    #message_display(str(deviation),440,120)
                    #message_display(" seconds",480,120)
                    #deviation_percentage = int((abs(acceleration - geuss)/time)*100)
                    #str(deviation_percentage)
                    #message_display("You'r deviation in percentage is",300,140)
                    #message_display(str(deviation_percentage),560,140)
                    #message_display("%",580,140)
                    #if deviation_percentage < 10:
                        #message_display("Very good",300,160)
            message_display(str(geuss),700,40)
            



        #message_display(str(acceleration),1,70 )
        #message_display("m/s^2",1,90)
        #message_display("\n You were off by ",1,110)
        #message_display(str(delevation),1,130)
        #message_display("You´r devition in percentage is",1,150)
        #message_display(str(deviation_percentage),1,170)
        #message_display("%",1,190)
        #if deviation_percentage < 10:
            #message_display("Very good",1,1)
        pygame.display.update()
pygame.quit()
