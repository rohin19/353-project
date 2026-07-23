from pyespn import PYESPN
import pandas as pd

season = 2025
espn = PYESPN('nba')
espn.load_season_rosters(season=season)
# espn.load_standings(season=season)
# store in dataframe
standings_df = pd.DataFrame(espn.load_standings(season=season))
print(standings_df)