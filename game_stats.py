import json


class GameStats:
    """Отслеживание статисктики для игры Target Shooting."""

    def __init__(self, ts_game):
        self.settings = ts_game.settings
        self.reset_stats()

        # Игра Target Shooting запускается в неактивном состоянии.
        self.game_active = False

        # Получает значение рекорда.
        self.high_score = self.get_high_score()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.bullets_left = self.settings.bullets_allowed
        self.score = 0

    def get_high_score(self):
        """Получает возвращаемое значение рекорда."""
        with open('high_score.json') as f:
            self.high_score = json.load(f)
        return self.high_score
