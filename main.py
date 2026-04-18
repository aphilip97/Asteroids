import pygame
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CENTRE_X, CENTRE_Y
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    print( f"Starting Asteroids with pygame version: {pygame.version.ver}" )
    print( f"Screen width: { SCREEN_WIDTH }" )
    print( f"Screen height: { SCREEN_HEIGHT }" )

    pygame.init()
    screen = pygame.display.set_mode( size=( SCREEN_WIDTH, SCREEN_HEIGHT ) )

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player = Player( x = CENTRE_X, y = CENTRE_Y )
    field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:

        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill( "black" )

        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)

        for thing in asteroids:
            if player.collides_with(thing):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        pygame.display.flip()

        dt = clock.tick( 60 ) / 1000

if __name__ == "__main__":
    main()
