import pygame

width = 1500
height = 700
#defining the colors and grid
white = (255,255,255)
green = (0,255,0)
black = (0,0,0)
block_size = 20

def makeSnake(size):
    pygame.draw.rect(screen, green, [], 0)

def main():
    
    #intitializing game window
    pygame.init()
    screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
    pygame.display.set_caption("Snake Game")
    
    
    #Game loop
    running = True
    while running:
        #Build the game world(Frontend)
        screen.fill(black)
        
        keys = pygame.key.get_pressed()
        #Get the ticks to show the time user has been playing the game
        ticks = (int)(pygame.time.get_ticks() / 1000)
        ticks += 1
        
        pygame.display.flip()
        
        #Exit sequence
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
main()

