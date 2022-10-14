import pygame
import sys
from settings import Settings
class AlienInvasion:
#overall class to manage game assets and behaviors

    def __init__(self):
        #initializes game and creates resources#
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.screen = pygame.display.set_mode((600, 400))
        self.bg_color=(0,0,0)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        #starts loop for the game
        self.screen.fill(self.settings.bg_color)
        while True:
            #watches for input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()
if __name__ == "__main__":
    #make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

