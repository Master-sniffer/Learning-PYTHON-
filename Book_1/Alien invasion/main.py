import pygame, sys
#my folders
from settings import Settings
from ship import Ship


class AlienInvasion:
    
    def __init__(self):
        """ИНИЦИАЛИЗАЦИЯ ИГРЫ"""
        pygame.init() #HERE IS EVERYTHING ALRIGHT
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("ALIEN INVASION")
        
        self.ship=Ship(self)

    def run_game(self):
        """ЗАПУСК ИГРЫ"""

        while True: #ОТСЛЕЖИВАНИЕ ДЕЙСТВИЙ С КЛАВЫ
            self._check_events()
            self._update_screen()

    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_colour)   
        self.ship.blitme()         
        pygame.display.flip()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()
