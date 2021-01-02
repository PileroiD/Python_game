import pygame
import sys
from time import sleep

from Alien_invasion.bullet import Bullet
from Alien_invasion.alien import Alien


########################################################################################################################
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    # Создание новой пули и включение ее в группу bullets.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings=ai_settings, screen=screen, ship=ship)
        bullets.add(new_bullet)


###########################################################################################

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


# ---------------------------------------------------------------------------------------------------------------------- check_play_button
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Запускает новую игру при нажатии кнопки Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        ai_settings.initialize_dynamic_settings()
        stats.game_active = True

        # Сброс изображения счетов уровня
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

    # Очистка списков пришельцев и пуль.
    aliens.empty()
    bullets.empty()
    # Создание нового флота и размещение корабля в центре.
    create_fleet(ai_settings=ai_settings, screen=screen, ship=ship, aliens=aliens)
    ship.center_ship()


# ---------------------------------------------------------------------------------------------------------------------- check_events
def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb):
    """Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:  # KEYDOWN
            check_keydown_events(event=event, ship=ship, ai_settings=ai_settings, screen=screen, bullets=bullets)

        elif event.type == pygame.KEYUP:  # KEYUP
            check_keyup_events(event=event, ship=ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings=ai_settings, screen=screen, stats=stats, play_button=play_button, ship=ship,
                              aliens=aliens, bullets=bullets, mouse_x=mouse_x, mouse_y=mouse_y, sb=sb)


# ---------------------------------------------------------------------------------------------------------------------- update_screen
def update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats, sb):
    """Обновляет изображения на экране и отображает новый экран."""
    screen.blit(ai_settings.bg_color, (0, 0))  # выводится задний фон

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    # Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()  # выводится корабль
    aliens.draw(screen)
    pygame.display.flip()


# ---------------------------------------------------------------------------------------------------------------------- update_bullets
def update_bullets(aliens, bullets, ai_settings, screen, ship, stats, sb):
    """Обновляет позиции пуль и уничтожает старые пули."""
    # Обновление позиций пуль.
    bullets.update()

    # Удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        check_bullet_alien_collisions(ai_settings=ai_settings, screen=screen, ship=ship, aliens=aliens, bullets=bullets,
                                      sb=sb, stats=stats)


# ---------------------------------------------------------------------------------------------------------------------- check_bullet_alien_collisions
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, sb, stats):
    # Проверка попаданий в пришельцев.
    # При обнаружении попадания удалить пулю и пришельца.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Уничтожение существующих пуль и создание нового флота.
        # Если весь флот уничтожен, начинается слудующий уровень
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings=ai_settings, screen=screen, ship=ship, aliens=aliens)


# ============================================================================================================================================= Ряды пришельцев

# ---------------------------------------------------------------------------------------------------------------------- get_number_rows
def get_number_rows(ai_settings, ship_height, alien_height):
    """Определяет количество рядов, помещающихся на экране"""
    available_space_y = (ai_settings.screen_width - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


# ---------------------------------------------------------------------------------------------------------------------- create_fleet MAIN
def create_fleet(ai_settings, screen, aliens, ship):
    """Создает флот пришельцев."""
    # Создание пришельца и вычисление количества пришельцев в ряду.
    # Интервал между соседними пришельцами равен одной ширине пришельца.

    alien = Alien(ai_settings=ai_settings, screen=screen)
    # alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings=ai_settings, alien_width=alien.rect.width)  # 27
    number_rows = get_number_rows(ai_settings=ai_settings, ship_height=ship.rect.height,
                                  alien_height=alien.rect.height)  # 6

    # Создание флота пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings=ai_settings, screen=screen, aliens=aliens, alien_number=alien_number,
                         row_number=row_number)


# ---------------------------------------------------------------------------------------------------------------------- get_number_aliens_x
def get_number_aliens_x(ai_settings, alien_width):
    """Вычисляет количество пришельцев в ряду."""
    available_space_x = ai_settings.screen_width - 2 * alien_width  # От всего размера экрана отнимаем размер корабля(по х)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


# ---------------------------------------------------------------------------------------------------------------------- create_alien
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Создает пришельца и размещает его в ряду"""
    # Создание пришельца и перемещение его в ряду
    alien = Alien(ai_settings=ai_settings, screen=screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


# ---------------------------------------------------------------------------------------------------------------------- update_aliens
def update_aliens(ai_settings, aliens, ship, stats, screen, bullets, sb):
    """Проверяет, достиг ли флот края экрана,
после чего обновляет позиции всех пришельцев во флоте."""
    check_fleet_edges(ai_settings=ai_settings, aliens=aliens)
    aliens.update()

    # Проверка коллизий "пришелец-корабль".
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings=ai_settings, stats=stats, screen=screen, ship=ship, aliens=aliens, bullets=bullets, sb=sb)

    # Проверяет, добрались ли пришельцы до нижнего края экрана.
    check_aliens_bottom(ai_settings=ai_settings, stats=stats, screen=screen, ship=ship, aliens=aliens, bullets=bullets,
                        sb=sb)


# ---------------------------------------------------------------------------------------------------------------------- check_fleet_edges
def check_fleet_edges(ai_settings, aliens):
    """Реагирует на достижение пришельцем края экрана."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


# ---------------------------------------------------------------------------------------------------------------------- change_fleet_direction
def change_fleet_direction(ai_settings, aliens):
    """Опускает весь флот и меняет направление флота."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


# ---------------------------------------------------------------------------------------------------------------------- ship_hit
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """Обрабатывает столкновения корабля с пришельцем"""
    # Уменьшение ships_left
    if stats.ships_left > 0:
        stats.ships_left -= 1

        # Обновление игровой информации
        sb.prep_ships()

        # Очистка списков пришельцев и пуль
        aliens.empty()
        bullets.empty()

        # Создание нового флота и размещение корабля в центре
        create_fleet(ai_settings=ai_settings, screen=screen, ship=ship, aliens=aliens)
        ship.center_ship()

        # Пауза
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


# ---------------------------------------------------------------------------------------------------------------------- check_aliens_bottom
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """Проверяет, добрались ли пришельцы до нижнего края экрана."""
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Происходит тоже, что и при столкновении с кораблем
            ship_hit(ai_settings=ai_settings, stats=stats, screen=screen, ship=ship, aliens=aliens, bullets=bullets, sb=sb)
            break


# ---------------------------------------------------------------------------------------------------------------------- check_high_score
def check_high_score(stats, sb):
    """Проверяет, появился ли новый рекорд."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
    sb.prep_high_score()
