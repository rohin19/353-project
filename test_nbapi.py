from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder, playbyplayv3
from nba_api.stats.library.parameters import Season, SeasonType
import pandas as pd

# Find Dallas
mavs = next(
    team for team in teams.get_teams()
    if team["abbreviation"] == "DAL"
)

# Fetch Dallas games
gamefinder = leaguegamefinder.LeagueGameFinder(
    team_id_nullable=mavs["id"],
    season_nullable=Season.default,
    season_type_nullable=SeasonType.regular,
    timeout=60,
)

games = gamefinder.get_normalized_dict()["LeagueGameFinderResults"]
latest_game = games[0]

game_id = latest_game["GAME_ID"]
print(f'Fetching {latest_game["MATCHUP"]}, game ID {game_id}')

# Fetch its play-by-play
pbp = playbyplayv3.PlayByPlayV3(
    game_id=game_id,
    timeout=60,
)

df = pbp.get_data_frames()[0]
df = df.drop(columns=["gameId", "actionNumber", "teamId", "videoAvailable", "actionId"])
# pd.set_option("display.max_colwidth", 250)
# pd.set_option("display.max_rows", 250)
# print(df.head())
# print(df.columns.tolist())

# save to csv file
df.to_csv(f"pbp_{game_id}.csv", index=False)