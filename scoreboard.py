import json

import pygame.font


class Scoreboard:
    """"Класс для вывода игровой информации."""

    def __init__(self, ts_game):
        """Инициализирует атрибуты подсчета очков."""
        self.ts_game = ts_game
        self.screen = ts_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ts_game.settings
        self.stats = ts_game.stats

        # Настройки шрифта для вывода счета.
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 48)
        # Подготовка изображений.
        self.prep_images()

    def prep_images(self):
        """Подготавливает данные статистики для вывода на экран."""
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""
        score = self.stats.score
        # Вставляет запятые при преобразовании числового значения в строку
        score_str = f"{score:,}"
        self.score_img = self.font.render(score_str, True, self.text_color)

        # Вывод счета в правой верхней части экрана.
        self.score_rect = self.score_img.get_rect()
        self.score_rect.midbottom = self.screen_rect.midbottom

    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение."""
        high_score = self.stats.high_score
        high_score_str = f"{high_score:,}"
        self.high_score_img = self.font.render(f'--- {high_score_str} ---', True, self.text_color)

        # Рекорд выравнивается по центру верхней стороны.
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 5

    def check_high_score(self):
        """Сравнивает текущий счет с рекордом."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def save_new_record(self):
        """Сохраняет новый рекорд в файл."""
        with open('high_score.json', 'w') as f:
            json.dump(self.stats.high_score, f)

    def show_score(self):
        """Выводит текущие очки и рекорд."""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
