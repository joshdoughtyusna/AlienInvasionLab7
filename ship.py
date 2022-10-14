import pygame

class Ship:
    def __init__(selfself,ai_game):
        self.screen = ai_game.screen
        self.screen_react = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/star-wars-2897280__480.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
    def blitme(selfself):
        self.screen.blit(self.image,self.rect)