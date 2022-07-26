from feedparser import *
from pprint import pprint
from datetime import datetime
from time import mktime
import json


RSS_URL = 'https://www.pravda.com.ua/rss/view_news/'
feed = parse(RSS_URL)

urls = [
    'pravda.com.ua',
    'epravda.com.ua',
    'life.pravda.com.ua',
    'eurointegration.com.ua'
]

pprint(feed['entries'][0])
news = []

data = {}
data['title'] = feed['entries'][0]['title']
data['summary'] = feed['entries'][0]['summary']
data['published'] = datetime.fromtimestamp(mktime(feed['entries'][0]['published_parsed'])).strftime("%m/%d/%Y, %H:%M:%S")
data['link'] = feed['entries'][0]['link']
data['post'] = ''

news.append(data)

with open('news.json', 'w') as f:
    json.dump(news, f, indent=4, sort_keys=True, ensure_ascii=True)



with open("news.json", 'r') as file:
    data = file.read()
    data = json.loads(data)
    pprint(data)