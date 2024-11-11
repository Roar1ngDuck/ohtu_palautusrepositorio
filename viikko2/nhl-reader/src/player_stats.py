from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, player_reader: PlayerReader):
        self._player_reader = player_reader

    def top_scorers_by_nationality(self, nationality: str):
        players = self._player_reader.get_players()
        finnish_players = filter(lambda player: player.nationality == nationality, players)
        for player in sorted(finnish_players, key=lambda player: player.goals + player.assists, reverse=True):
            yield player