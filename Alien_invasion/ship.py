import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, screen, ai_settings):
        super(Ship, self).__init__()
        """Инициадизирует корабль и задает его начальную позицию"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('C:\\Programming\\Python\\my_programs\\Alien_invasion\\images\\ship.png')
        self.rect = self.image.get_rect()  # Создается surface изображения корабля
        self.screen_rect = screen.get_rect()  # Создается surface всего игрового окна

        """Каждый новый корабль появляется у нижнего края экрана"""
        self.rect.centerx = self.screen_rect.centerx  # По центру
        self.rect.bottom = self.screen_rect.bottom  # В самый низ экрана
        self.center = float(self.rect.centerx)  # 64

        """Флаг перемещения корабля"""
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_left and self.rect.left + 40 > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_right and self.rect.right - 40 < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        # Обновление атрибута rect на основании self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней стороны"""
        self.center = self.screen_rect.centerx
