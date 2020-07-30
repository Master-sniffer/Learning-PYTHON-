import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings #получили настройки, как экземпляр, чтобы возни было меньше (К настройкам мы обращаемся так -> переменная self.settings -> игра.settings -> получаем настройки (settings))
        self.screen_rect=ai_game.screen.get_rect() #Узнали размер экрана 

        self.image=pygame.image.load('images/4f3e72d669bedd4022000045.bmp')
        self.rect=self.image.get_rect() #узнали размер картинки

        self.rect.midbottom=self.screen_rect.midbottom #закинули расположение  объектма на Середину дна

        self.x=float(self.rect.x) #запихнули текущее расположение корабля в переменную
        self.y=float(self.rect.y)

        #moving is down here
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
    
    def update(self): #обновление движения в зависимости от клавиши
        if self.moving_right and self.rect.right<=self.screen_rect.right:
            self.x+=self.settings.ship_speed
        elif self.moving_left and self.rect.left>=0:
            self.x-=self.settings.ship_speed
        if self.moving_up and self.rect.top>0:
            self.y-=self.settings.ship_speed
        elif self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.y+=self.settings.ship_speed
        
        self.rect.x=self.x #
        self.rect.y=self.y
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
