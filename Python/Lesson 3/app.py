import requests
from pprint import pprint


URL = "https://api.covid19api.com/summary"

covid19_data = requests.get(URL)

covid19_global = covid19_data.json()['Global']
covid19_countries = covid19_data.json()['Countries']
titles = ['Country','NewConfirmed','NewDeaths','NewRecovered',
         'TotalConfirmed', 'TotalDeaths', 'TotalRecovered']

for item in titles:
    if item == 'Country':
        print("{0:_^32s}".format(item),end='')
    else:
        print("{0:_^20s}".format(item),end='')
print(end="\n")

for item in covid19_countries:
    for key in item:
        if key in titles:
            if key == 'Country':
                print("{0:<32s}".format(item[key]),end='')
            else:
                print("{0:>20}".format(item[key]),end='')
    print(end="\n")