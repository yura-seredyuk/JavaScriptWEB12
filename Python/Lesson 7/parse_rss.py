from feedparser import *
from pprint import pprint
from datetime import datetime
from time import mktime
import json

from pravda_parser import parser

RSS_URL = 'https://www.pravda.com.ua/rss/view_news/'
feed = parse(RSS_URL)

urls = [
    'pravda.com.ua',
    'epravda.com.ua',
    'life.pravda.com.ua',
    'eurointegration.com.ua'
]

news = []
for item in feed['entries']:

    data = {}
    data['title'] = item['title']
    data['summary'] = item['summary']
    data['published'] = datetime.fromtimestamp(mktime(item['published_parsed'])).strftime("%m/%d/%Y, %H:%M:%S")
    data['link'] = item['link']
    if data['link'].split('/')[2][4:] == 'pravda.com.ua':
        data['post'] = parser(data['link'])
        news.append(data)
    #     break
    # else: continue   
    # elif  data['link'].split('/')[2][4:] == 'epravda.com.ua':
    #     data['post'] = parser_epr(data['link'])
    #     news.append(data)

    

with open('news.json', 'w') as f:
    json.dump(news, f, indent=4, sort_keys=True, ensure_ascii=True)

with open("news.json", 'r') as file:
    data = file.read()
    data = json.loads(data)
    # pprint(data)