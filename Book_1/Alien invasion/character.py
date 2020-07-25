import pygame

class Character():
    def __init__(self, ai_game):
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        self.image=pygame.image.load('images/sci-fi-3144558_960_720.bmp')
        self.rect=self.image.get_rect()

        self.rect.midleft=self.screen_rect.midleft
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)