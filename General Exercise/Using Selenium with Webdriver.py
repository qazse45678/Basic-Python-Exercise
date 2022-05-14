from bs4 import BeautifulSoup
from selenium import webdriver

try:
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	chrome = webdriver.Chrome(options=options, executable_path='/Users/ryan/tmp/chromedriver')
	chrome.set_page_load_timeout(10)
	chrome.get('[https://code-gym.github.io/spider_demo/](https://code-gym.github.io/spider_demo/)')
	soup = BeautifulSoup(chrome.page_source, 'html5lib')
	print(soup.find('h1').text)
	chrome.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div/div/h3/a').click()
	print(chrome.find_element_by_xpath('//*[@id="post-header"]/div[2]/div/div/h1').text)

finally:
	chrome.quit()
