"""
'prevda.com.ua' parser
"""
import requests
from bs4 import BeautifulSoup


def parser(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    article = soup.find('article', class_="post")
    post_text = article.find('div', class_="post_text")
    data = {}
    data['content'] = []
    element = post_text.find('p')
    data['content'].append({'p':element.text.strip()})
    while element != None:
        element = element.find_next_sibling()
        if element == None: break
        if element.name == 'p':
            if element.text.strip() == '': continue
            data['content'].append({'p':element.text.strip()})
        elif element.name == 'div' and 'post__video' in element['class']:
            iframe = element.find('iframe')
            data['content'].append({'iframe':iframe.get('src')})
        elif element.name == 'div' and 'image-box' in element['class']:
            img = element.find('img')
            if img == None: continue
            data['content'].append({'img':img.get('src')})
        elif 'h' in element.name:
            data['content'].append({'h2':element.text.strip()})
        # elif element.name == 'ul':
        # ul=[]
        # for li in element.find_all('li'):
        #     ul.append({'li':li.text.strip()})
        #     pass
        #     data['content'].append({'ul':[]element.find_all('li')})    

    print(data)
    return data

if __name__ == "__main__":
    pass