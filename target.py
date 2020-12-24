import pygame


class Target:
    """Класс, представляющий мишень."""

    def __init__(self, ai_game):
        """Инициализирует мишень и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.color = self.settings.target_color
        self.dist_times = self.settings.distance_times

        # Отрисовка мишени и назначение атрибута rect.
        self.rect = pygame.Rect(0, 0, self.settings.target_width, self.settings.target_height)
        self.rect.center = self.screen_rect.center

        # Сохранение точной вертикальной позиции мишени.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Перенаправляет мишень, если объект находится у края экрана."""
        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        """Перемещает мишень вверх или вниз."""
        self.y += self.settings.target_speed * self.settings.target_direction
        self.rect.y = self.y

    def draw_target(self):
        """Вывод мишени на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def start_position_target(self):
        """Назначает мишени исходную позицию."""
        self.rect.center = self.screen_rect.center
        self.y = float(self.rect.y)
        self.color = self.settings.target_color

    def increase_distance(self):
        """Увеличивает дальность мишени."""
        if (self.rect.x * self.dist_times) < self.screen_rect.right:
            self.rect.x *= self.dist_times
