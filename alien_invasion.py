import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """ Overall class to manage game assets and behavior """

    def __init__(self):
        """ Initialize the game, and create game resources. """
        pygame.init()
        self.settings = Settings()

        # Set display window size
        if (self.settings.use_fullscreen):
            self.screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height)
            )

        #pygame.display.set_caption("Alien Invasion")
        pygame.display.set_caption("Posey Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _update_screen(self):
        # Redraw the screen during each pass through the loop. Update images
        # on the screen, and flip to the new screen.
        self.screen.fill(self.settings.bg_color)
        # Draw the ship at its current location
        self.ship.blitme()
        # Draw the bullets in the bullets group
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _check_events(self):
        """ Respond to keypresses and mouse events. """
        # Watch for keyboard and mouse events (event loop).
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Respond to keypresses. """
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ Respond to key releases. """
        if event.key == pygame.K_RIGHT:
            # Stop moving the ship to the right.
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            # Stop moving the ship to the left.
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group. """
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

        
#
# MAIN BODY OF PROGRAM
#

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai=AlienInvasion()
    ai.run_game()