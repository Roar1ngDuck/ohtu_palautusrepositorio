import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_player_name_correct(self):
        player = self.stats.search("Lemieux")
        self.assertEqual(player.name, "Lemieux")

    def test_search_player_team_correct(self):
        players = self.stats.search("Lemieux")
        self.assertEqual(players.team, "PIT")

    def test_search_player_goals_correct(self):
        players = self.stats.search("Lemieux")
        self.assertEqual(players.goals, 45)

    def test_search_player_assists_correct(self):
        players = self.stats.search("Lemieux")
        self.assertEqual(players.assists, 54)

    def test_search_player_points_correct(self):
        players = self.stats.search("Lemieux")
        self.assertEqual(players.points, 99)

    def test_search_non_existing_player(self):
        player = self.stats.search("Non existing player")
        self.assertEqual(player, None)

    def test_search_team_all_players(self):
        players = self.stats.team("EDM")
        names = sorted([player.name for player in players])
        self.assertEqual(names, ["Gretzky", "Kurri", "Semenko"])

    def test_search_non_existing_team(self):
        players = self.stats.team("Non existing team")
        self.assertEqual(len(players), 0)

    def test_top_three_players(self):
        players = self.stats.top(2)
        names = sorted([player.name for player in players])
        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])