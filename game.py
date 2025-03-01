import pygame
from sys import exit

pygame.init()
#defining the colors and grid
width = 800
height = 600
white = (255,255,255)
green = (6, 82, 3)
black = (0,0,0)
block_size = 20
font1_size1 = pygame.font.Font('Font/Kablammo/Kablammo-Regular-VariableFont_MORF.ttf',50)
font1_size2 = pygame.font.Font('Font/Kablammo/Kablammo-Regular-VariableFont_MORF.ttf',64)
font1_size3 = pygame.font.Font('Font/Kablammo/Kablammo-Regular-VariableFont_MORF.ttf',24)

#function to make text surface
def text_surface(screen,text,x,y,width,hieght,color,size):
    if(size == 1):
        font = font1_size1
    elif(size == 2):
        font = font1_size2
    else:
        font = font1_size3
    pygame.draw.rect(screen,color,(width,width,hieght,hieght))
    textSurface = font.render(text,True,(0,0,0))
    screen.blit(textSurface, (x,y))
    
    
def mainmenu(screen):
    screen.fill(green)
    text_surface(screen,"Snake Game",230,118,230,150,green,2)
    text_surface(screen,"Play",360,280,250,50,green,1)
    text_surface(screen,"Quit",375,415,120,30,green,3)
    
    
def main():
    #intitializing game window
    pygame.init()
    screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    
    #defining Custom Events
    
    
    #Game loop
    while True:
        mainmenu(screen)
        for event in pygame.event.get():
            #Exit sequence
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()    
            
        #Get the ticks to show the time user has been playing the game
        ticks = (int)(pygame.time.get_ticks() / 1000)
        ticks += 1
        
        #Updating the changes
        pygame.display.update()
        clock.tick(60)
        


main()

