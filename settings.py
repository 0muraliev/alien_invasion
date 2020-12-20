class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.bg_color = (24, 32, 37)

        # Настройки корабля
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (240, 40, 40)
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.fleet_drop_speed = 10

        # Темп ускорения игры.
        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        # Настройки корабля
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0

        # 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Подсчет очков.
        self.alien_points = 5

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
