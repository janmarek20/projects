class GameStats:
    """Monitorowanie danych statystycznych w grze "Inwazja obcych"."""

    def __init__(self, ai_game):
        """Inicjalizacja danych statystycznych."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Uruchomienie gry "Inwazja obcych" w stanie aktywnym.
        self.game_active = False

        # Najlepszy wynik nigdy nie powinien zostać wyzerowany.
        self.high_score = 0

    def reset_stats(self):
        """Inicjalizacja danych statystycznych w trakcie gry."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1