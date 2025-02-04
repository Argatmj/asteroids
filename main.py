import pygame
from constants import *
from player import * 

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    p1 = player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        p1.update(dt)
        p1.draw(screen)

        pygame.display.flip()
        dt = time.tick(60) / 1000

if __name__ == "__main__":
    main()