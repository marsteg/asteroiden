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
    pygame.display.set_caption('Astroids')
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

    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    black = (0, 0, 0)
    fontsize = 24
    font = pygame.font.Font('freesansbold.ttf', fontsize)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

       # draw the score
        scoreString = "Score: " + str(player.score)
        scoreText = font.render(scoreString, True, blue, white)
        scoreTextRect = scoreText.get_rect()
        scoreTextRect.topright = (SCREEN_WIDTH, 2)
        screen.blit(scoreText, scoreTextRect)

        # draw the lives
        livesString = "Lives: " + str(player.lives)
        livesText = font.render(livesString, True, blue, white)
        livesTextRect = livesText.get_rect()
        livesTextRect.topright = (SCREEN_WIDTH, fontsize + 5)
        screen.blit(livesText, livesTextRect)


        # update all objects
        for updatable_object in updatable:
            updatable_object.update(dt)

        # check for collisions
        for asteroid in asteroids:
            if player.collides_with(asteroid) and asteroid.initialized: 
                if player.lives > 0:
                    player.lives -= 1
                    print("Player lives: ", player.lives)
                    player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    player.velocity = pygame.Vector2(0, 0)
                    player.rotation = 0
                    continue
                print("Game Over!")
                print("collided with asteroid ", asteroid.id ," on position: " + str(asteroid.position))
                print("Score: ", player.score)
                sys.exit(0)
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    player.scoreUp()
                    shot.kill()
        
        for ship in ships:
            if player.collides_with(ship) and ship.initialized:
                print("Game Over!")
                print("collided with ship ", ship.id ," on position: " + str(ship.position))
                showFinalScore(player.score, screen)
                sys.exit(0)
            for shot in shots:
                if ship.collides_with(shot):
                    ship.split()
                    player.scoreUp()
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


def showFinalScore(score, screen):
	color = (148, 33, 228)
	font = pygame.font.Font('freesansbold.ttf', 50)
	text = font.render('Score: %s' % score, True, color)
	rect = text.get_rect()
	rect.center = screen.get_rect().center
	screen.blit(text, rect)