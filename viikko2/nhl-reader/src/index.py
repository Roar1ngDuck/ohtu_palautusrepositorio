import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN:")

    finnish_players = filter(lambda player: player.nationality == "FIN", players)
    for player in sorted(finnish_players, key=lambda player: player.goals + player.assists, reverse=True):
        print(player)

if __name__ == "__main__":
    main()