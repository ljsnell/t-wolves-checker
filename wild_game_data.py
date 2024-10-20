# https://api-web.nhle.com/v1/standings/now
import requests
from datetime import datetime, timedelta

# s/o this post: https://stackoverflow.com/questions/30483977/python-get-yesterdays-date-as-a-string-in-yyyy-mm-dd-format
def yesterday(frmt='%Y-%m-%d', string=True):
    yesterday = datetime.now() - timedelta(1)
    if string:
        return yesterday.strftime(frmt)
    return yesterday

def get_wins_from_standings(contents):
    for standing in contents['standings']:
        # print(standing["teamName"])
        # print(standing["teamName"]["default"])
        team_name = standing["teamName"]["default"]
    
        if team_name == "Minnesota Wild":
            return standing["wins"]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
base_url = 'https://api-web.nhle.com/v1/standings/'
todays_url = base_url + 'now'
yesterdays_url = base_url + yesterday()

todays_contents = requests.get(todays_url,headers).json()
yesterdays_contents = requests.get(yesterdays_url,headers).json()

todays_win_total = get_wins_from_standings(todays_contents)
yesterdays_win_total = get_wins_from_standings(yesterdays_contents)

if todays_win_total != yesterdays_win_total:
    print(f"Today's win total: {todays_win_total}")
    print(f"Yesterday's win total: {yesterdays_win_total}")
    print("Use code: WILDWIN for 50% off pizzas online only")
else:
    print('No Pizza Today 😔')
