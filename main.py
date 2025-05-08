import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # set containers for Player class
    Player.containers = (updatable, drawable)

    # set containers for Asteroid class
    Asteroid.containers = (asteroids, updatable, drawable)

    # set static containers for AsteroidField class
    AsteroidField.containers = updatable

    # set containers for Shot class
    Shot.containers = (shots, updatable, drawable)

    # create an instance of AsteroidField
    asteroid_field = AsteroidField()

    # create player after setting containers
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            shot = player.shoot() # call player's shoot method
            if shot:
                shots.add(shot) # add the returned Shot to the shots group
        
        updatable.update(dt)

        # check for collisions between player and asteroids
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                import sys
                sys.exit()

        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
