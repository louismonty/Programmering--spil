import pygame
from ball_drop import gameloop_bd
#from Acceleration import gameloop_ac

screen_width = 1000
screen_hight = 1000
#Initialize screen
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_hight))
pygame.display.init() 
#colors
white = [253, 254, 254]
red = [255, 87, 51]
gray = [202, 207, 210]
#makes boxes color gray
game_one_color = gray
game_to_color = gray
game_one = False
game_to = False
#font of tekst 
font = pygame.font.SysFont("Times New Roman",30)

#Text editor
def message_display(text,x_text,y_text):
    text_surf = font.render(text,True,([0,0,0]))
    screen.blit(text_surf,[x_text,y_text])
#Gameloop
run = True
while run:
    #Makes game run in loop 
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            run=False
        #makes screen go white 
        screen.fill(white)
        #draws boxes 
        pygame.draw.polygon (screen, game_one_color, [(300, 200), (650, 200), (650, 400), (300, 400)])
        pygame.draw.polygon (screen, game_to_color, [(300, 500), (650, 500), (650, 700), (300, 700)])
        #draws tekst in box
        message_display("hej",310,290)
        message_display("hej",310,590)
        pygame.display.update()
        mouse_pos_x = (pygame.mouse.get_pos()[0])
        mouse_pos_y = (pygame.mouse.get_pos()[1])
        #print(mouse_pos_x,mouse_pos_y)

        #Checking if the mouse is in the box
        if (mouse_pos_x >=300 and mouse_pos_x <=650) and (mouse_pos_y >=200 and mouse_pos_y <= 400 ):
            game_one = True
            #start the game
            if (event.type == pygame.MOUSEBUTTONDOWN):
                screen.fill(white)
                gameloop_bd()
        else:
            game_one = False  

        #Checking if the mouse is in the box
        if (mouse_pos_x >=300 and mouse_pos_x <=650) and (mouse_pos_y >=500 and mouse_pos_y <= 700 ):
            game_to = True
            #start the game
            if (event.type == pygame.MOUSEBUTTONDOWN):
                screen.fill(white)
                gameloop_ac()
        else:
            game_to = False           

        pygame.mouse.get_pos()

        #makes the box red or gray
        if game_one == True:
            game_one_color = red 
        else:
            game_one_color = gray
        
        if game_to == True:
            game_to_color = red 
        else:
            game_to_color = gray     

pygame.quit()