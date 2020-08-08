#import this # delete the first hashtag to see the truth
import pygame, sys, json
from time import sleep
#my folders
from settings import Settings
from ship import Ship
from bullet import Bullet
from game_stats import GameStats
from alien import Alien
from button import Button
from scoreboard import Scoreboard
#from character import Character



class AlienInvasion:
    
    def __init__(self):
        """ИНИЦИАЛИЗАЦИЯ ИГРЫ"""
        pygame.init() #HERE IS EVERYTHING ALRIGHT
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  # 4
        self.screen_rect=self.screen.get_rect()
        # ЕС ХОТИТЕ СДЕЛАТЬ НА ФУЛ ЭКРАН - УБИРАЙТЕ # В 1 , 2 , 3 ПУНКТЕ И ПОСТАВЬТЕ # В 4 ПУНКТЕ
        # self.screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)  # 1
        # self.settings.screen_width=self.screen.get_rect().width        # 2
        # self.settings.screen_height=self.screen.get_rect().height      # 3
        pygame.display.set_caption("ALIEN INVASION")
        

        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.stats=GameStats(self)
        self.sb=Scoreboard(self)
        self.aliens=pygame.sprite.Group() #объявление группы пришельцев 
        #self.charecter=Character(self) # MB I WILL DO IT

        self._create_fleet()#при первом вызыове 
        self.play_button=Button(self,"LETS START")

        self.filename="saved_data.json"

    def run_game(self):
        """ЗАПУСК ИГРЫ"""

        while True: #ОТСЛЕЖИВАНИЕ ДЕЙСТВИЙ С КЛАВЫ
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()
            self._update_screen()

    
    def _update_screen(self): #отвечает за то, что вообще на экране творится
        self.screen.fill(self.settings.bg_colour) #Заполнить экран определенным цветом
        self.ship.blitme() # Использовать метод показа корабля 
        #self.charecter.blitme()  #MB I WILL DO IT  
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)#показывает пришельцев на self.screen (общий экран)
        if not self.stats.game_active:
            self.play_button.draw_button()
        self.sb.show_score() #Метод показа очков
        pygame.display.flip() #обновление экрана 


    def _check_events(self): #общая проверка ивентов
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keyDOWN(event)
               
            elif event.type==pygame.KEYUP:
                self._check_keyUP(event)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    
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
            some_score=self.stats.high_score
            with open (self.filename, "w") as f: #Открытие файла 
                print ("d") #Лоигрование, что запись в файл идет
                json.dump(some_score, f) #Сохранение результата
            sys.exit()
        
        elif event.key==pygame.K_SPACE: #Вызов метода стрельбы пули
            self._fire_bullet()
    
    def _check_keyUP(self, event): #проверка, какую клавишу отпустили  (или отпущена)
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False
        elif event.key==pygame.K_UP:
            self.ship.moving_up=False
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=False
    
    def _check_play_button(self, mouse_pos):
        button_clicked=self.play_button.rect.collidepoint(mouse_pos) #проверка нажатия кнопки 
        if button_clicked and not self.stats.game_active: #если кнопка нажата и игра не запущена начинается игра 
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active=True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            pygame.mouse.set_visible(False) #Метод, чтобы мышка исчезла

    def _fire_bullet(self): #отвечает за запуск пули
        if len(self.bullets) < self.settings.bullet_allowed: #Если длина меньше кол-во разрешенных пуль 
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullet(self): #отвечает за устраниение пули, когда она достигнет определенной точки
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
        #print (len(self.bullets))
        self._check_bullet()

    def _check_bullet(self):
        collisions=pygame.sprite.groupcollide(self.bullets, self.aliens, False, True) #Проверка взаимодействия группы пули и группы пришельцев
        if collisions: #Если есть коллизия
            for aliens in collisions.values():
                self.stats.score+=self.settings.alien_score*len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens: #Если группа пришельцев пустая
            self.bullets.empty() 
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level+=1
            self.sb.prep_level()

    def _ship_hit(self): #Проверка был ли удра корабля
        if self.stats.ships_left>=0: #Если кол-во кораблей больше или равно нулю - продолжать действие 
            self.stats.ships_left-=1 
            self.sb.prep_ships()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship() 

            sleep(0.5) #Остановить игру на 0.5 сек
        else:
            self.stats.game_active=False
            pygame.mouse.set_visible(True)

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
        alien_width, alien_height=alien.rect.size #Сначала идет ширина потом длина пришельца
        alien.x=alien_width+2* alien_width * alien_number #определили расстояние между инепрешеленцами
        alien.rect.x=alien.x #Расположение пришельца 
        alien.rect.y=alien_height +2*alien_height*row
        self.aliens.add(alien) #добавление пришельца в "список пришельцев"

    def _create_alien_1(self, alien_number, row): 
        alien=Alien(self)
        alien_width, alien_height=alien.rect.size
        alien.x=alien_width+alien_width+2* alien_width * alien_number 
        alien.rect.x=alien.x
        alien.rect.y=2*alien_height*row
        self.aliens.add(alien)

    def _update_aliens(self):
        self.aliens.update()
        
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._aliens_check_bottom()
        self._check_fleet()

    def _aliens_check_bottom(self): #Проверка достиг ли пришелец дна 
        for alien in self.aliens.sprites():
            if alien.rect.bottom>=self.screen_rect.bottom:
                self._ship_hit()
                break
    
    def _check_fleet(self): #Проверка дошел ли пришелец до края
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_direction()
                break
    
    def _change_direction(self): #Смена направления 
        for alien in self.aliens.sprites(): #меняем направление каждого пришельца с помощью группы спрайт
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *=-1
    

if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()

