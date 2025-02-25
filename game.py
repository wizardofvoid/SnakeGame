import pygame

#defining the colors and grid
white = (255,255,255)
green = (0,255,0)
black = (0,0,0)
block_size = 20

# def draw_snake(snake_body):
    

def main():
    
    #intitializing game window
    pygame.init()
    screen = pygame.display.set_mode((600,400),pygame.RESIZABLE)
    pygame.display.set_caption("Snake Game")
    
    #Game loop
    running = True
    while running:
        screen.fill(black)
        pygame.draw.rect(screen, green, pygame.Rect(block_size,block_size,block_size,block_size))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
main()

