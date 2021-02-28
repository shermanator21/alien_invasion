class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        # Read in all time high score
        f = open("high_score.txt", "r")
        perma_high_score = int(f.readline())

        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state
        self.game_active = False

        # High score should never be reset
        self.high_score = perma_high_score
        self.level = 1

        # close file
        f.close()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
