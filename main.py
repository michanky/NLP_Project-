import praw
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from transformers import pipeline
import config as cfg
import scraper as sc

summarizer = pipeline("summarization")
reddit = praw.Reddit(
    client_id=cfg.CLIENT_ID,
    client_secret=cfg.CLIENT_SECRET,
    user_agent=cfg.USER_AGENT,
    username=cfg.USERNAME,
    password=cfg.PASSWORD
)  # Login to Reddit


def generate_chunks(inp_str):  # generate chunks for long articles
    max_chunk = 500
    inp_str = inp_str.replace('.', '.<eos>')
    inp_str = inp_str.replace('?', '?<eos>')
    inp_str = inp_str.replace('!', '!<eos>')

    sentences = inp_str.split('<eos>')
    current_chunk = 0
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1:
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])
    return chunks


subreddit = reddit.subreddit('articlessgtest')
tmp_list = []
for post in subreddit.new(limit=None):
    if sc.unique_check(post.url) and post.url not in tmp_list:
        tmp_list.append(post.url)
        article = sc.extract_domain(post.url)
        chunks = generate_chunks(article)
        res = summarizer(chunks, max_length=150,
                         min_length=50, do_sample=False)
        text = ' '.join([summ['summary_text'] for summ in res])
        post.reply(text)
        # comment out article
    else:
        continue
