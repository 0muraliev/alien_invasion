import json

import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """"Класс для вывода игровой информации."""

    def __init__(self, ai_game):
        """Инициализирует атрибуты подсчета очков."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Настройки шрифта для вывода счета.
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 48)
        # Подготовка изображений.
        self.prep_images()

    def prep_images(self):
        """Подготавливает данные статистики для вывода на экран."""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""
        score = self.stats.score
        # Вставляет запятые при преобразовании числового значения в строку
        score_str = f"{score:,}"
        self.score_img = self.font.render(score_str, True, self.text_color)

        # Вывод счета в правой верхней части экрана.
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение."""
        high_score = self.stats.high_score
        high_score_str = f"{high_score:,}"
        self.high_score_img = self.font.render(high_score_str, True, self.text_color)

        # Рекорд выравнивается по центру верхней стороны.
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Сравнивает текущий счет с рекордом."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def save_new_record(self):
        """Сохраняет новый рекорд в файл."""
        with open('high_score.json', 'w') as f:
            json.dump(self.stats.high_score, f)

    def prep_level(self):
        """Преобразует уровень в графическое изображение."""
        lvl_str = str(self.stats.level)
        self.lvl_img = self.font.render('lvl ' + lvl_str, True, self.text_color)

        # Уровень выводится под текущим счетом.
        self.lvl_rect = self.lvl_img.get_rect()
        self.lvl_rect.right = self.score_rect.right
        self.lvl_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Сообщает количество оставшихся кораблей."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Выводит очки, уровень и количество кораблей на экран."""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.lvl_img, self.lvl_rect)
        self.ships.draw(self.screen)
