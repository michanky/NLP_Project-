from bs4 import BeautifulSoup
import urllib3
from selenium import webdriver
import time
import sqlite3


def unique_check(url):  # check if url is already inserted
    unique = True
    con = sqlite3.connect('TestDB.db')
    try:
        with con:
            con.execute('INSERT INTO URL VALUES (?)', (url,))
            print('URL inserted successfully!')
            return unique
    except sqlite3.IntegrityError:
        print('URL already exists')
        unique = False
        return unique


def scraper_ST(url):  # extract url from Straits Times
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, 'html.parser')
    bucket = ''
    for item in soup.findAll('div', attrs={'class': 'odd field-item'}):
        for p in item.findAll('p'):
            bucket += p.text
            bucket += ' '
    return bucket


def scraper_today(url):  # extract url from Today
    bucket = ''
    browser = webdriver.Firefox()
    browser.get(url)
    # Today requires a browser in order to run, this is a chokepoint
    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html, features='html.parser')
    for item in soup.findAll('div', attrs={'id': 'article_detail_body'}):
        for p in item.findAll('p'):
            bucket += p.text
            bucket += ' '
    browser.quit()
    return bucket


def extract_domain(url):  # extract the domain and call scrape function on respective domain
    if 'todayonline' in url[:30]:
        return scraper_today(url)
    elif 'straitstimes' in url[:30]:
        return scraper_ST(url)
    else:
        print('DOMAIN NOT FOUND')
