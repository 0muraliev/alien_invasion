import pygame.font

from settings import Settings


class Button:
    """Инициализация атрибутов кнопки."""

    def __init__(self, ts_game, msg):
        self.settings = Settings()
        self.screen = ts_game.screen
        self.screen_rect = self.screen.get_rect()

        # Назначение размеров и свойств кнопок.
        self.width, self.height = 80, 50
        self.button_color = self.settings.bg_color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 58)

        # Построение объекта rect кнопки и выравнивание в центре экрана.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Сообщение кнопки создается только один раз.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Отображение пустой кнопки и вывод текста.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
