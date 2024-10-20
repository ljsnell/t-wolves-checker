from nba_api.live.nba.endpoints import scoreboard

# # Today's Score Board
games = scoreboard.ScoreBoard()

# # json
games.get_json()

print(games.get_json())
