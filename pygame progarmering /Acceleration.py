import pygame
import math
import os
from random import randint

#Definitons
screen_width = 1100
screen_hight = 1000
screen = pygame.display.set_mode((screen_width,screen_hight))
#Initialize screen
pygame.display.init() 
pygame.init()
#Font for tekst
font = pygame.font.SysFont("Times New Roman",30)
#Make screen white
screen.fill([255,255,255])

#Text editor
def message_display(text,x_text,y_text):
    text_surf = font.render(text,True,([0,0,0]))
    screen.blit(text_surf,[x_text,y_text])

#Gameloop
def gameloop_ac():
    run = True
    geuss = ""
    #Randome time
    time = randint(1,20)
    #Calgulates acceleration 
    acceleration = ((40/3.6)/time)
    while run:
        #Makes game run in loop 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

            start_print ="A car is in a race and the green light is turning on, the car reaches 40km/h at "
            start_print += str(time)
            start_print += " seconds"
            message_display(str(start_print),1,1)
            message_display("At which acceleration do you the think the car will gain?: ",1,40)
            #Checks if a button is pressed
            if (event.type==pygame.KEYDOWN):
                #Checks if 1 key is pressed
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
                    #Deletes the texst 
                if (event.key==pygame.K_BACKSPACE):
                    screen.fill([255,255,255])
                    geuss = ""
                    #Write a comma
                if (event.key==pygame.K_COMMA):
                    geuss += "."
                    #Checks if enter key is pressed
                if (event.key==pygame.K_RETURN):
                    #rounds up time
                    time = round(time,2)
                    #add´s the tekst togeter 
                    acceleration_print = "Acceleration is "
                    acceleration_print += str(round(acceleration,2))
                    acceleration_print += " m/s^2"
                    #prints the tekst 
                    message_display(acceleration_print,300,100)
                    deviation_print = "You were off by "
                    deviation_print += str(abs(round(acceleration-float(geuss),2)))
                    deviation_print += " m/s^2"
                    message_display(deviation_print,300,130)
                    deviation_percentage = int((abs(acceleration - float(geuss))/time)*100)
                    deviation_percentage_print = "You´r devition in percentage is "
                    deviation_percentage_print += str(deviation_percentage)
                    deviation_percentage_print += "%"
                    message_display(deviation_percentage_print,300,160)

            message_display(str(geuss),700,40)
            
        pygame.display.update()
#gameloop_ac()
pygame.quit()

