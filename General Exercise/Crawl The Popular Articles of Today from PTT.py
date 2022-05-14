import requests
from bs4 import BeautifulSoup
import time

def pttNBA(url):
    resp = requests.get(url) #'https://www.ptt.cc/bbs/NBA/index.html'
    
    #防錯
    if resp.status_code != 200:
        print('發生錯誤' + url)
        return
    
    soup = BeautifulSoup(resp.text, 'html5lib')
    paging = soup.find_all('a',{'class': 'btn', 'class': 'wide'})[1]['href']
    today = time.strftime('%m/%d').lstrip('0')
    articles = []
    
    for i in soup.find_all('div','r-ent'):
        number = i.find('div','nrec').text.strip()
        title = i.a.string.strip()
        date = i.find('div','meta').find('div','date').string.strip()
        article = number + title + date
        
        try:
            if date == today and int(number) > 10:
                articles.append(article)
        except:
            if date == today and number == '爆':
                articles.append(article)
    
    if len(articles) != 0:
        for article in articles:
            print(article)
        pttNBA('https://www.ptt.cc' + paging)
    else:
        return
                
pttNBA('https://www.ptt.cc/bbs/NBA/index.html')
