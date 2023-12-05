from nba_api.stats.endpoints import leaguegamefinder

# Query for games where the Wolves were playing
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=1610612750)
# The first DataFrame of those returned is what we want.
games = gamefinder.get_data_frames()[0]
three_pts_made = games.at[0,'FG3M']

print(three_pts_made)
if(three_pts_made) > 11:
    print('3 pts made: ' + three_pts_made)
