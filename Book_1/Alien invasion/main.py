import sys
import pygame


class AlienInvasion:
    
    def __init__(self):
        """ИНИЦИАЛИЗАЦИЯ ИГРЫ"""
        pygame.cdrom.init()

        self.screen=pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("ALIEN INVASION")
        self.bg_color=(230,230,230)

    def run_game(self):
        """ЗАПУСК ИГРЫ"""

        while True: #ОТСЛЕЖИВАНИЕ ДЕЙСТВИЙ С КЛАВЫ
            for event in pygame.event.get():
                if event.type==pygame.cdrom.quit():
                    sys.exit()
                
            self.screen.fill(self.bg_color)
            
            pygame.display.flip()

if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()
