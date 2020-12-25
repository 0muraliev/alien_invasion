import pygame


class Ship:
    """Класс для управления кораблем."""

    def __init__(self, ts_game):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ts_game.screen
        self.settings = ts_game.settings
        self.screen_rect = ts_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется посередине у левого края экрана.
        self.rect.midleft = self.screen_rect.midleft

        # Сохранение вещественной координаты центра корабля.
        self.y = float(self.rect.y)

        self._movement_flags()

    def _movement_flags(self):
        """Флаги перемещения корабля."""
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флагов."""
        # Обновляется атрибут y, не rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Обновление атрибута y на основании self.y
        self.rect.y = self.y

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def start_position_ship(self):
        """Размещает корабль посередине левого края экрана."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
