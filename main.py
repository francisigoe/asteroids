import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import *
from logger import log_state


def main():
    print("Starting Asteroids with pygame version: VERSION")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:" , SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field_1 = AsteroidField()

    Player.containers = (updatable, drawable)
    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field_1 = AsteroidField()
    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
        
        updatable.update(dt)
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        dt = (time.tick(60)) / 1000

            


if __name__ == "__main__":
    main()
