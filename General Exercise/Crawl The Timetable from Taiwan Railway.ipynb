{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "304e1d9b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "insert general table\n",
      "insert shooting table\n"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "import requests\n",
    "import json\n",
    "\n",
    "custom_headers = {\n",
    "    'Host': 'stats.nba.com',\n",
    "    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',\n",
    "    'Accept': 'application/json, text/plain, */*',\n",
    "    'Accept-Language': 'en-US,en;q=0.5',\n",
    "    'Accept-Encoding': 'gzip, deflate, br',\n",
    "    'x-nba-stats-origin': 'stats',\n",
    "    'x-nba-stats-token': 'true',\n",
    "    'Connection': 'keep-alive',\n",
    "    'Referer': 'https://stats.nba.com/',\n",
    "    'Pragma': 'no-cache',\n",
    "    'Cache-Control': 'no-cache',\n",
    "}\n",
    "\n",
    "connection = sqlite3.connect('/Users/marylin/文件/SQL/NBA.db')\n",
    "cursor = connection.cursor()\n",
    "\n",
    "try:\n",
    "    gen_url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='\n",
    "    gen_response = requests.get(gen_url, headers = custom_headers)\n",
    "    gen_datas = json.loads(gen_response.text)\n",
    "    print('insert general table')\n",
    "    \n",
    "    for gen_data in gen_datas['resultSets'][0]['rowSet']:\n",
    "        cursor.execute('insert into nba_general(player_id, player_name, gp, pts, fgm, fga, fg_per) values (?, ?, ?, ?, ?, ?, ?)', \n",
    "                   (gen_data[0], gen_data[1], gen_data[5], gen_data[29], gen_data[10], gen_data[11], gen_data[12]))\n",
    "        \n",
    "    sho_url = 'https://stats.nba.com/stats/leaguedashplayershotlocations?College=&Conference=&Country=&DateFrom=&DateTo=&DistanceRange=By+Zone&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='\n",
    "    sho_resp = requests.get(sho_url, headers=custom_headers)\n",
    "    sho_datas = json.loads(sho_resp.text)\n",
    "    print('insert shooting table')\n",
    "    for sho_data in sho_datas['resultSets']['rowSet']:\n",
    "        cursor.execute('insert into nba_shooting (player_id, res_fgm, res_fga, res_fg_per, pai_fgm, pai_fga, pai_fg_per, mid_fgm, mid_fga, mid_fg_per, left3_fgm, left3_fga, left3_fg_per, right3_fgm, right3_fga, right3_fg_per, pt3_fgm, pt3_fga, pt3_fg_per) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',\n",
    "                    (sho_data[0], sho_data[5], sho_data[6], sho_data[7], sho_data[8], sho_data[9], sho_data[10], sho_data[11], sho_data[12], sho_data[13], sho_data[14], sho_data[15], sho_data[16], sho_data[17], sho_data[18], sho_data[19], sho_data[20], sho_data[21], sho_data[22]))\n",
    "        \n",
    "    connection.commit()  \n",
    "    \n",
    "finally:\n",
    "    connection.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f3e0e255",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "import requests\n",
    "import json\n",
    "\n",
    "custom_headers = {\n",
    "    'Host': 'stats.nba.com',\n",
    "    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',\n",
    "    'Accept': 'application/json, text/plain, */*',\n",
    "    'Accept-Language': 'en-US,en;q=0.5',\n",
    "    'Accept-Encoding': 'gzip, deflate, br',\n",
    "    'x-nba-stats-origin': 'stats',\n",
    "    'x-nba-stats-token': 'true',\n",
    "    'Connection': 'keep-alive',\n",
    "    'Referer': 'https://stats.nba.com/',\n",
    "    'Pragma': 'no-cache',\n",
    "    'Cache-Control': 'no-cache',\n",
    "}\n",
    "\n",
    "connection = sqlite3.connect('/Users/marylin/文件/SQL/NBA.db')\n",
    "cursor = connection.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ec224ec",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
