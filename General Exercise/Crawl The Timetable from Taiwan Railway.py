import requests
from bs4 import BeautifulSoup
import time

url = 'https://tip.railway.gov.tw/tra-tip-web/tip'

def getTrip():
    resp = requests.get('https://tip.railway.gov.tw/tra-tip-web/tip') #'https://tip.railway.gov.tw/tra-tip-web/tip'
    
    try:
        #防錯
        if resp.status_code != 200:
            print('發生錯誤' + url)

        soup = BeautifulSoup(resp.text, 'html5lib')
        today = time.strftime('%Y/%m/%d')
        station = soup.find(id = 'cityHot').ul.find_all('li')
        stationDic = {}

        #站名 & 站碼
        for i in station:
            stationName = i.text.strip()
            stationId = i.button['title']
            stationDic[stationName] = stationId

        #準備傳送資料
        csrf = soup.find('input', {'name': '_csrf'})['value']
        startStation = input('請輸入出發地：')
        endStation = input('請輸入目的地：')

        formData = {
            '_csrf': csrf,
            'trainTypeList': 'ALL',
            'transfer': 'ONE',
            'startStation': stationDic[startStation],
            'endStation': stationDic[endStation],
            'rideDate': today,
            'startOrEndTime': 'true',
            'startTime': '00:00',
            'endTime': '23:59',
        }

        #傳送資料
        url = soup.find(id = 'queryForm')['action']
        answerResp = requests.post('https://tip.railway.gov.tw/' + url, data = formData)
        answerSoup = BeautifulSoup(answerResp.text, 'html5lib')

        #從回傳的資料中，取出重點（車次、時間）
        trainOption = answerSoup.find_all('tr','trip-column')
        for i in trainOption:
            trainId = i.a.text
            startTrain = i.find_all('span','location')[0].text
            endTrain = i.find_all('span','location')[1].text
            startTime = i.find_all('td')[1].text
            endTime = i.find_all('td')[2].text

            print(trainId + '(' + startTrain + '→' + endTrain + ')' + ' 出發時間：' + startTime + ' 抵達時間：' + endTime)

    except KeyError:
        print('地點輸入錯誤')

getTrip()
