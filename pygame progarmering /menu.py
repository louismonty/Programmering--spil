import pygame
from ball_drop import gameloop_bd
#from Acceleration import gameloop_ac

screen_width = 1000
screen_hight = 1000
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_hight))
pygame.display.init() 
white = [253, 254, 254]
red = [255, 87, 51]
gray = [202, 207, 210]
game_one_color = gray
game_to_color = gray
game_one = False
game_to = False
font = pygame.font.SysFont("Times New Roman",30)

def message_display(text,x_text,y_text):
    text_surf = font.render(text,True,([0,0,0]))
    screen.blit(text_surf,[x_text,y_text])

run = True
while run:
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            run=False
        screen.fill(white)
        pygame.draw.polygon (screen, game_one_color, [(300, 200), (650, 200), (650, 400), (300, 400)])
        pygame.draw.polygon (screen, game_to_color, [(300, 500), (650, 500), (650, 700), (300, 700)])
        message_display("hej",310,290)
        message_display("hej",310,590)
        pygame.display.update()
        mouse_pos_x = (pygame.mouse.get_pos()[0])
        mouse_pos_y = (pygame.mouse.get_pos()[1])
        #print(mouse_pos_x,mouse_pos_y)

        if (mouse_pos_x >=300 and mouse_pos_x <=650) and (mouse_pos_y >=200 and mouse_pos_y <= 400 ):
            game_one = True
            if (event.type == pygame.MOUSEBUTTONDOWN):
                screen.fill(white)
                gameloop_bd()
        else:
            game_one = False  


        if (mouse_pos_x >=300 and mouse_pos_x <=650) and (mouse_pos_y >=500 and mouse_pos_y <= 700 ):
            game_to = True
            if (event.type == pygame.MOUSEBUTTONDOWN):
                screen.fill(white)
                gameloop_ac()
        else:
            game_to = False           

        pygame.mouse.get_pos()

        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_DOWN):
                game_to = True 
                game_one = False

            if (event.type==pygame.K_RETURN):
                print("x")
                screen.fill([255,255,255])

            if (event.key==pygame.K_UP):
                game_to = False 
                game_one = True


        if game_one == True:
            game_one_color = red 
        else:
            game_one_color = gray
        
        if game_to == True:
            game_to_color = red 
        else:
            game_to_color = gray     

pygame.quit()