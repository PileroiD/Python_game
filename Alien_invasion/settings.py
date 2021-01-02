import pygame


class Settings:

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 640
        self.screen_height = 960
        self.bg_color = pygame.image.load('C:\\Programming\\Python\\my_programs\\Alien_invasion\\images\\phon.bmp')

        # Корабль
        self.ship_speed_factor = 4
        self.ship_limit = 3

        # Пришельцы
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Пуля:
        self.bullet_speed_factor = 5
        self.bullet_width = 1
        self.bullet_height = 50
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 10

        # Темп ускорения игры
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 1
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
