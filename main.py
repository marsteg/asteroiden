import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from moon import *
from ship import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    ships = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    Moon.containers = (updatable, drawable)
    Ship.containers = (updatable, drawable, ships)
    asteroidfield = AsteroidField()
    moon = Moon()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))


        # update all objects
        for updatable_object in updatable:
            updatable_object.update(dt)

        # check for collisions
        for asteroid in asteroids:
            if player.collides_with(asteroid) and asteroid.initialized: 
                print("Game Over!")
                print("collided with asteroid ", asteroid.id ," on position: " + str(asteroid.position))
                sys.exit(0)
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
        
        for ship in ships:
            if player.collides_with(ship) and ship.initialized:
                print("Game Over!")
                print("collided with ship ", ship.id ," on position: " + str(ship.position))
                sys.exit(0)
            for shot in shots:
                if ship.collides_with(shot):
                    ship.split()
                    shot.kill()
                    


        # draw all objects
        for drawable_object in drawable:
            drawable_object.draw(screen)
        # update the display
        pygame.display.flip()
        # limit the frame rate
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()