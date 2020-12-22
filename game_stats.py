import json


class GameStats:
    """Отслеживание статисктики для игры Alien Invasion."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False

        # Получает значение рекорда.
        self.high_score = self.get_high_score()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def get_high_score(self):
        """Получает возвращаемое значение рекорда."""
        with open('high_score.json') as f:
            self.high_score = json.load(f)
        return self.high_score
