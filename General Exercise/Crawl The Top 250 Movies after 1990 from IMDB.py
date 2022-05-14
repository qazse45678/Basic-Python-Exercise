from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random

url = 'https://www.imdb.com/chart/top/?sort=rk,asc&mode=simple&page=1'

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    
    #使用 chromedriver 打開 chrome 網頁
    chrome = webdriver.Chrome(options = options, executable_path = '/Users/marylin/chromedriver')
    #chrome.set_page_load_timeout(10)
    
    #開始抓分頁資料
    chrome.get(url)
    soup = BeautifulSoup(chrome.page_source, 'html5lib')
    listing = soup.find('tbody', 'lister-list').find_all('tr')
    for i in listing:
        name = i.find('td','titleColumn').a.string
        year = i.find('td','titleColumn').span.string
        year_num = year.split('(').pop().split(')')[0]
        rating = i.find('td','imdbRating').strong.string
        
        if float(year_num) > 1990:
            result = name + year + '' + rating
            print(name, year, rating)
        
    
finally:
    chrome.quit()
