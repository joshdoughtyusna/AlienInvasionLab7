import pygame
import sys
from settings import Settings
from ship import Ship


class AlienInvasion:
    # overall class to manage game assets and behaviors

    def __init__(self):
        # initializes game and creates resources#
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.screen = pygame.display.set_mode((600, 400))
        self.bg_color = (120, 120, 120)
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        # starts loop for the game
        self.screen.fill(self.settings.bg_color)
        while True:
            # watches for input
            self.check_events()
            self.ship.update()
            self.update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                   self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
