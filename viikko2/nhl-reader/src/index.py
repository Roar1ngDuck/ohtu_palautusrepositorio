from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table

def main():
    console = Console()

    console.print("[i]NHL statistics by nationality[/i]\n")

    console.print("Select season [purple][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25][/purple]: ", end="")
    season = input()
    console.print()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationalities = set([player.nationality for player in reader.get_players()])

    while (True):
        console.print(f"Select nationality [purple][{'/'.join(nationalities)}][/purple]: ", end="")
        nationality = input()

        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Top scorers of {nationality} season {season}")
        table.add_column("name", style="bold")
        table.add_column("team", style="bold")
        table.add_column("goals", style="bold", justify="right")
        table.add_column("assists", style="bold", justify="right")
        table.add_column("points", style="bold", justify="right")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals + player.assists))

        console.print(table)
        console.print()

if __name__ == "__main__":
    main()