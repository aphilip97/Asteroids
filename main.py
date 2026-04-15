import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CENTRE_X, CENTRE_Y
from logger import log_state
from player import Player

def main():

    print( f"Starting Asteroids with pygame version: {pygame.version.ver}" )
    print( f"Screen width: { SCREEN_WIDTH }" )
    print( f"Screen height: { SCREEN_HEIGHT }" )

    pygame.init()
    screen = pygame.display.set_mode( size=( SCREEN_WIDTH, SCREEN_HEIGHT ) )

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player( x = CENTRE_X, y = CENTRE_Y )

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

        pygame.display.flip()

        dt = clock.tick( 60 ) / 1000

if __name__ == "__main__":
    main()
