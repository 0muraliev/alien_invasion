import sys

import pygame

from game_stats import GameStats
from target import Target
from bullet import Bullet
from button import Button
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Создание экземпляра для хранения игровой статистики.
        self.stats = GameStats(self)

        # Создается экземпляр корабля, мишени и группа снарядов
        self.ship = Ship(self)
        self.target = Target(self)
        self.bullets = pygame.sprite.Group()

        # Создание кнопки Play.
        self.play_button = Button(self, 'Play')

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_target()

            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Сброс игровой статистики и начало новой.
            self._start_game()

    def _start_game(self):
        """Начинает игру и скрывает курсор мыши."""
        self.stats.game_active = True
        pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p and not self.stats.game_active:
            self._start_game()
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Если в запасе есть снаряд, то включаем его в группу bullets."""
        if self.stats.bullets_left:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.stats.bullets_left -= 1
        else:
            self._bullets_limit()

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        self.bullets.update()

        for bullet in self.bullets:
            if bullet.rect.right >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
        self._check_bullet_target_collisions()

    def _update_target(self):
        """
        Проверяет, достигла ли мишень края экрана,
        с последующим обновлением позиций.
        """
        self._check_target_edges()
        self.target.update()

        if pygame.sprite.spritecollideany(self.target, self.bullets):
            self._bullets_limit()

    def _check_target_edges(self):
        """Реагирует на достижение мишени края экрана."""
        if self.target.check_edges():
            self._change_target_direction()

    def _change_target_direction(self):
        if self.target.check_edges():
            self.settings.target_direction *= -1

    def _check_bullet_target_collisions(self):
        """Обнаружение коллизий снарядов с мишенью."""
        if pygame.sprite.spritecollide(self.target, self.bullets, True):
            self.target.increase_distance()

    def _bullets_limit(self):
        self.stats.game_active = False
        self.bullets.empty()
        self.ship.start_position_ship()
        self.target.start_position_target()
        self.stats.reset_stats()
        pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.target.draw_target()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Кнопка Play отображается в том случае, если игра неактивна.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
