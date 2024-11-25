class TennisGame:
    MIN_SCORE_FOR_ADVANTAGE = 4
    SCORE_DIFFERENCE_FOR_ADVANTAGE = 1
    SCORE_DIFFERENCE_FOR_WIN = 2

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        match player_name:
            case self.player1_name:
                self.player1_points += 1
            case self.player2_name:
                self.player2_points += 1
            case _:
                raise ValueError("Invalid player name")

    def get_score(self):
        if self.player1_points == self.player2_points:
            return self.get_score_for_tie()
        elif max(self.player1_points, self.player2_points) >= self.MIN_SCORE_FOR_ADVANTAGE:
            return self.get_score_for_advantage_or_win()
        else:
            return self.get_score_for_no_advantage()

    def get_score_for_tie(self):
        match self.player1_points:
            case 0:
                return "Love-All"
            case 1:
                return "Fifteen-All"
            case 2:
                return "Thirty-All"
            case _:
                return "Deuce"

    def get_score_for_advantage_or_win(self):
        player_score_difference = abs(self.player1_points - self. player2_points)

        if player_score_difference == self.SCORE_DIFFERENCE_FOR_ADVANTAGE:
            if self.player1_points > self.player2_points:
                return f"Advantage {self.player1_name}"
            else:
                return f"Advantage {self.player2_name}"

        if player_score_difference >= self.SCORE_DIFFERENCE_FOR_WIN:
            if self.player1_points > self.player2_points:
                return f"Win for {self.player1_name}"
            else:
                return f"Win for {self.player2_name}"

    def get_score_for_no_advantage(self):
        player1_score = self.get_score_for_no_advantage_by_points(self.player1_points)
        player2_score = self.get_score_for_no_advantage_by_points(self.player2_points)
        return f"{player1_score}-{player2_score}"
    
    def get_score_for_no_advantage_by_points(self, player_points):
        match player_points:
            case 0:
                return "Love"
            case 1:
                return "Fifteen"
            case 2:
                return "Thirty"
            case 3:
                return "Forty"