import pygame, sys
#my folders
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
#from character import Character



class AlienInvasion:
    
    def __init__(self):
        """ИНИЦИАЛИЗАЦИЯ ИГРЫ"""
        pygame.init() #HERE IS EVERYTHING ALRIGHT
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width=self.screen.get_rect().width
        # self.settings.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("ALIEN INVASION")
        
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        #self.charecter=Character(self) # MB I WILL DO IT

        self._create_fleet()

    def run_game(self):
        """ЗАПУСК ИГРЫ"""

        while True: #ОТСЛЕЖИВАНИЕ ДЕЙСТВИЙ С КЛАВЫ
            self._check_events()
            self.ship.update()
            self._update_bullet()
            self._update_screen()

    
    def _update_screen(self): #отвечает за то, что вообще на экране творится
        self.screen.fill(self.settings.bg_colour)   
        self.ship.blitme()    
        #self.charecter.blitme()  #MB I WILL DO IT  
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


    def _check_events(self): #общая проверка ивентов
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keyDOWN(event)
               
            elif event.type==pygame.KEYUP:
                self._check_keyUP(event)

    
    def _check_keyDOWN(self, event): #проверка нажатой клавиши
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=True   
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=True 
        if event.key==pygame.K_UP:
            self.ship.moving_up=True
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=True
        elif event.key==pygame.K_ESCAPE: #стоп слово
            sys.exit()
        
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyUP(self, event): #проверка, какую клавишу отпустили  ( или отпущена)
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False
        elif event.key==pygame.K_UP:
            self.ship.moving_up=False
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=False
    
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)

        #print (len(self.bullets))

    def _create_fleet(self):
        alien=Alien(self)
        self.aliens.add(alien)



if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()

