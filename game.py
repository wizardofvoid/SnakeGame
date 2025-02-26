import pygame

#defining the colors and grid
white = (255,255,255)
green = (0,255,0)
black = (0,0,0)
block_size = 20

    

def main():
    
    #intitializing game window
    pygame.init()
    screen = pygame.display.set_mode((600,400),pygame.RESIZABLE)
    pygame.display.set_caption("Snake Game")
    
    #Game loop
    running = True
    while running:
        #Color the game world
        screen.fill(black)
        
        #Get the ticks to show the time user has been playing the game
        ticks = (int)(pygame.time.get_ticks() / 1000)
        print(ticks)
        ticks += 1
        
        pygame.display.flip()
        
        #Exit sequence
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
main()

