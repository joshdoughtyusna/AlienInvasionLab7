import pygame
import sys
class AlienInvasion:
#overall class to manage game assets and behaviors

    def __init__(self):
        #initializes game and creates resources
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color=(0,230,0)
        pygame.display.set_caption("Alien Invasion")
    def run_game(self):
        #starts loop for the game
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
