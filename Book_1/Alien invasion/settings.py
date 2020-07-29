class Settings():
    def __init__(self):
        self.screen_width=1280
        self.screen_height=800
        self.bg_colour=(210,230,230)
        #параметр корабля
        self.ship_limit=3
        #параметр пришельца
        self.fleet_drop_speed=10
        #ПАРАМЕТР СНАРЯДА
        self.bullet_width=5
        self.bullet_height=15
        self.bullet_color=(50,50,20)
        self.bullet_allowed=5
        #Темп ускорения игры
        self.speed_scale=1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3.0
        self.alien_speed_factor=1.0
        self.fleet_direction=1
