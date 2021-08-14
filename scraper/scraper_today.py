from selenium import webdriver
from bs4 import BeautifulSoup
import time

bucket = ''
browser = webdriver.Firefox()
url = 'https://www.todayonline.com/singapore/69-year-old-singaporean-man-dies-covid-19-complications-6th-such-death-august-death-toll'
browser.get(url)
time.sleep(20)  # wait 20 seconds for the site to load.
html = browser.page_source
soup = BeautifulSoup(html, features='html.parser')
for item in soup.findAll('div', attrs={'id': 'article_detail_body'}):
    for p in item.findAll('p'):
        bucket += p.text
        bucket += ' '
browser.quit()
print(bucket)
