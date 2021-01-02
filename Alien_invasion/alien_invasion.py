import pygame
from pygame.sprite import Group

from Alien_invasion import game_function as gf
from Alien_invasion.button import Button
from Alien_invasion.game_stats import GameStats
from Alien_invasion.score_board import Scoreboard
from Alien_invasion.settings import Settings
from Alien_invasion.ship import Ship


def run_game():
    """Инициализирует игру и создает объект экрана"""
    pygame.init()

    ai_settings = Settings()  # настройки

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(screen=screen, ai_settings=ai_settings)  # корабль

    stats = GameStats(ai_settings=ai_settings)

    sb = Scoreboard(ai_settings=ai_settings, screen=screen, stats=stats)

    play_button = Button(ai_settings=ai_settings, screen=screen, msg='Play')

    # Создание корабля, группы пуль и группы пришельцев.
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings=ai_settings, screen=screen, aliens=aliens, ship=ship)
    """Основной цикл игры"""
    while True:
        gf.check_events(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets, play_button=play_button,
                        stats=stats, aliens=aliens, sb=sb)  # Смотрит за событиями

        if stats.game_active:
            ship.update()  # Обновление позиции корабля

            gf.update_aliens(aliens=aliens, ai_settings=ai_settings, ship=ship, stats=stats, screen=screen,
                             bullets=bullets, sb=sb)  # Обновляет позиции всех пришельцев на экране

            gf.update_bullets(aliens=aliens, bullets=bullets, ai_settings=ai_settings, screen=screen,
                              ship=ship, stats=stats, sb=sb)  # Обновление позици пули и её удаление привыходе за окно игры

        # bullets.update()  # Перемещение пули

        gf.update_screen(ai_settings=ai_settings, screen=screen, ship=ship, aliens=aliens,
                         bullets=bullets, play_button=play_button, stats=stats, sb=sb)  # Обновление окна игры

        # pygame.time.delay(10)


run_game()
