class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.bg_color = (24, 32, 37)

        # Настройки корабля
        self.ship_speed = 1.5

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (240, 40, 40)
        self.bullets_allowed = 5
