import praw
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from transformers import pipeline
import config as cfg

summarizer = pipeline("summarization")
reddit = praw.Reddit(
    client_id=cfg.CLIENT_ID,
    client_secret=cfg.CLIENT_SECRET,
    user_agent=cfg.USER_AGENT,
    username=cfg.USERNAME,
    password=cfg.PASSWORD
)
dictionary_of_websites = {'Today': [], 'ST': []}

subreddit = reddit.subreddit('articlessgtest')

for post in subreddit.new(limit=None):
    if 'todayonline' in post.url:
        dictionary_of_websites['Today'].append([post.url])
    elif 'straitstimes' in post.url:
        dictionary_of_websites['ST'].append(post.url)
    else:
        print('Not valid URL')

print('Successfully extracted Valid URLs')
print(dictionary_of_websites)

# bucket = ''
# for keys in dictionary_of_websites.keys():
#     if len(dictionary_of_websites[keys]) != 0:
#         if keys == 'Today':
#             for url in dictionary_of_websites[keys]:
#                 article = ''
#                 # open browser to activate script to get the content
#                 browser = webdriver.Firefox()
#                 browser.get(url)
#                 time.sleep(20)  # wait 10 seconds for the site to load.
#                 html = browser.page_source  # get the html
#                 soup = BeautifulSoup(html, features='html.parser')
#                 for item in soup.findAll('div', attrs={'id': 'article_detail_body'}):
#                     for p in item.findAll('p'):
#                         article += p.text
#                         article += ' '
#                 print(article)
#                 print('Finish printing one article')
#                 browser.quit()
# print(bucket)

# while True:
#     #run everything
#     time.sleep(86400)
