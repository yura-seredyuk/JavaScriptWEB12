import requests
from bs4 import BeautifulSoup

# URL = 'https://scrapingclub.com/exercise/list_basic/?page=1'

# response = requests.get(URL)

# soup = BeautifulSoup(response.text, 'lxml')

# items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

# print(items)
# print(len(items))

# for i, item in enumerate(items, start=1):
#     itemName = item.find('h4', class_="card-title").text.strip()
#     itemPrice = item.find('h5').text
#     # if float(item.find('h5').text[1:]) > 50:
#     #     continue
#     itemImage = item.find('img').get('src')
#     print(f'{i}: {itemPrice} -- {itemName} (https://scrapingclub.com{itemImage})')


URL = 'https://scrapingclub.com'

response = requests.get(URL+'/exercise/list_basic/?page=1')

soup = BeautifulSoup(response.text, 'lxml')
paginator = soup.find('ul', class_="pagination")
links = paginator.find_all('li', class_="page-item")
last_page = 0
for item in links[::-1]:
    if item.text.strip().isdigit():
        last_page = int(item.text.strip())
        break

for page in range(1,last_page+1):
    newUrl = f'{URL}/exercise/list_basic/?page={page}'
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i, item in enumerate(items, start=1):
        itemName = item.find('h4', class_="card-title").text.strip()
        itemPrice = item.find('h5').text
        itemImage = item.find('img').get('src')
        print(f'Page {page} {i}: {itemPrice} -- {itemName} ({URL+itemImage})')
