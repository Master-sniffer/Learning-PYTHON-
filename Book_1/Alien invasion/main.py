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
        self.aliens=pygame.sprite.Group() #объявление группы пришельцев 
        #self.charecter=Character(self) # MB I WILL DO IT

        self._create_fleet()#при первом вызыове 

    def run_game(self):
        """ЗАПУСК ИГРЫ"""

        while True: #ОТСЛЕЖИВАНИЕ ДЕЙСТВИЙ С КЛАВЫ
            self._check_events()
            self.ship.update()
            self._update_bullet()
            self._update_aliens()
            self._update_screen()

    
    def _update_screen(self): #отвечает за то, что вообще на экране творится
        self.screen.fill(self.settings.bg_colour)   
        self.ship.blitme()    
        #self.charecter.blitme()  #MB I WILL DO IT  
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)#показывает пришельцев на self.screen (общий экран)
        pygame.display.flip() #обновление экрана 


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
    
    def _fire_bullet(self): #отвечает за запуск пули
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullet(self): #отвечает за устраниение пули, когда она достигнет определенной точки
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)

        #print (len(self.bullets))

    def _create_fleet(self): #Создание флота пришельцев 
        alien=Alien(self)
        alien_width, alien_height=alien.rect.size #метод alien.rect.size возвращает ширину и длину пришельца
        ship_height=self.ship.rect.height #высота корабля
        available_space_x=self.settings.screen_width-(2*alien_width) #настройки экрана - ширина пришельца * 2 (чтобы было место)
        available_space_y=self.settings.screen_height-(3* alien_height) - ship_height #получаем настройки, чтобы узнать кол-во рядов, мы можем сделать
        number_rows=available_space_y//(2*alien_height) #считаем точное кол-во, чтобы у игрока был шанс нормально играть без проблем
        number_aliends=available_space_x//(2*alien_width) #кол-во пришельцев в ряду
        for row in range ((number_rows-2)//2): #допилить вариацию ряда
            for number in range(number_aliends): # вводим цикл для каждого пришельца 
                self._create_alien(number,row) #для каждого нового пришельца, мы вызываем метод создания пришельца (указываем кол-во в ряду и кол-во рядом)
                self._create_alien_1(number,row+1)

    def _create_alien(self, alien_number,row): # создание пришельца 
        alien=Alien(self)
        alien_width, alien_height=alien.rect.size
        alien.x=alien_width+2* alien_width * alien_number #определили расстояние между инепрешеленцами
        alien.rect.x=alien.x
        alien.rect.y=alien_height +2*alien_height*row
        self.aliens.add(alien) #добавление пришельца в "список пришельцев"

    def _create_alien_1(self, alien_number, row):
        alien=Alien(self)
        alien_width, alien_height=alien.rect.size
        alien.x=alien_width+alien_width+2* alien_width * alien_number 
        alien.rect.x=alien.x
        alien.rect.y=alien_height=2*alien_height*row
        self.aliens.add(alien)

    def _update_aliens(self):
        self.aliens.update()
        self._check_fleet()
    
    def _check_fleet(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_direction()
                break
    
    def _change_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *=-1

if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()

