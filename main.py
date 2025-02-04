import pygame
import sys
from constants import *
from player import * 
from asteroid import * 
from asteroidfield import * 

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    player.containers = (updatable,drawable)
    asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (updatable,drawable,shots)
    p1 = player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ast = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        updatable.update(dt)
        for astr in asteroids:
            if p1.collision(astr):
                sys.exit("Game Over")
            for bullet in shots:
                if bullet.collision(astr):
                    astr.split()


        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = time.tick(60) / 1000

if __name__ == "__main__":
    main()