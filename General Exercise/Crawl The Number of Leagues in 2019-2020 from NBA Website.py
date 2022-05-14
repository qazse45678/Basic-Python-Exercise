import requests

url = 'https://data.nba.net/prod/v2/2019/teams.json'
request_url = requests.get(url)
response = request_url.json()
team = response['league']['standard']
nba_num = 0

for i in range(len(team)):
    if team[i]['isNBAFranchise'] == True:
        nba_num += 1

print('2019 - 2020 球季 NBA 有 {} 支隊伍 '.format(nba_num))
