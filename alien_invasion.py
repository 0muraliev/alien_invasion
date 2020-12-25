import random
import sys
from time import sleep

import pygame

from bullet import Bullet
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
from target import Target


class TargetShooting:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Target Shooting")

        self._create_instances_and_groups()

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_target()

            self._update_screen()

    def _create_instances_and_groups(self):
        """Создает экземпляры и группы объектов, необходимые для работы игры."""

        # Экземпляры для хранения игровой статистики и панели результатов.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Экземпляры корабля, мишени и группы снарядов.
        self.ship = Ship(self)
        self.target = Target(self)
        self.bullets = pygame.sprite.Group()

        # Экземпляр кнопки Play.
        self.play_button = Button(self, 'Play')

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.sb.save_new_record()
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
            self._start_game()

    def _start_game(self):
        """
        Сбрасывает статистику, начинает игру, подготавливает данные статистики и
        скрывает курсор мыши.
        """
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_images()
        pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if self.stats.game_active:
            if event.key == pygame.K_UP:
                self.ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                self.ship.moving_down = True
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()
        if event.key == pygame.K_q:
            self.sb.save_new_record()
            sys.exit()

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

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        self.bullets.update()

        for bullet in self.bullets:
            if bullet.rect.left > self.screen.get_rect().right:
                self.bullets.remove(bullet)
                if not self.bullets and not self.stats.bullets_left:
                    sleep(0.8)
                    self._bullets_limit()

        self._check_bullet_target_collisions()

    def _update_target(self):
        """
        Проверяет, достигла ли мишень края экрана,
        с последующим обновлением позиций.
        """
        self._check_target_edges()
        self.target.update()

    def _check_target_edges(self):
        """Реагирует на достижение мишени края экрана."""
        if self.target.check_edges():
            self._change_target_direction()

    def _change_target_direction(self):
        """Меняет направление движения мишени."""
        if self.target.check_edges():
            self.settings.target_direction *= -1

    def _check_bullet_target_collisions(self):
        """Обнаружение коллизий снарядов с мишенью."""
        collisions = pygame.sprite.spritecollide(self.target, self.bullets, True)
        if collisions:
            # Увеличивает расстояние от мишени
            self.target.increase_distance()

            # Прибавляет снаряды к запасу
            self.stats.bullets_left += 3

            # Увеличивает текущий счет
            self.stats.score += self.settings.target_points
            self.sb.prep_score()
            self.sb.check_high_score()

            # Меняет цвет мишени на случайное
            def r(): return random.randint(0, 255)
            self.target.color = r(), r(), r()

    def _bullets_limit(self):
        """Переводит игру в неактивную, когда закончатся все снаряды корабля."""
        self.stats.game_active = False
        self.ship.start_position_ship()
        self.target.start_position_target()

        # Сброс настроек.
        self.settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.target.draw_target()

        # Вывод информации о счете.
        self.sb.show_score()

        # Кнопка Play отображается в том случае, если игра неактивна.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ts = TargetShooting()
    ts.run_game()
