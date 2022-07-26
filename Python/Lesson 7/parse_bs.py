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
i = 0
for page in range(1,last_page+1):
    newUrl = f'{URL}/exercise/list_basic/?page={page}'
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i, item in enumerate(items, start=i+1):
        itemLink = item.select_one('h4 a').get("href")
        response = requests.get(URL+itemLink)
        soup_item = BeautifulSoup(response.text, 'lxml')
        itemName = soup_item.find('h3', class_="card-title").text.strip()
        itemPrice = soup_item.find('h4').text
        itemImage = soup_item.find('img', class_="card-img-top img-fluid").get('src')
        itemDetails = soup_item.find('p',class_="card-text").text.strip()
        print(f'Page {page} {i}: {itemPrice} -- {itemName} \n\t {itemDetails} \n\t ({URL+itemImage}), {URL+itemLink}')
