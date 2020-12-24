class Settings:
    """Класс для хранения всех настроек игры Target Shooting."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.bg_color = (24, 32, 37)

        # Настройки корабля
        self.ship_speed = 1.0

        # Параметры снаряда
        self.bullet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (240, 40, 20)
        self.bullets_allowed = 5

        # Параметры мишени
        self.distance_times = 1.1
        self.target_speed = 0.5
        self.target_width = 5
        self.target_height = 30
        self.target_color = (255, 255, 255)

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        # 1 обозначает движение вверх; а -1 - вниз.
        self.target_direction = 1
        self.target_points = 5
