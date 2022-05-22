import requests
from pprint import pprint


URL = "https://api.covid19api.com/summary"

covid19_data = requests.get(URL)



covid19_global = covid19_data.json()['Global']

covid19_countries = covid19_data.json()['Countries']
titles = ['Country','NewConfirmed','NewDeaths','NewRecovered',
         'TotalConfirmed', 'TotalDeaths', 'TotalRecovered']

task = 1
country = 'Zambia'


for item in titles:
    if item == 'Country':
        if task == 4: continue
        print("{0:_^32s}".format(item),end='')
        
    else:
        print("{0:_^20s}".format(item),end='')
print(end="\n")

newlist = sorted(covid19_countries, key=lambda d: d['NewConfirmed'], reverse=True) # task 2

# for item in covid19_countries:
for item in newlist:
# if True:
    # if country == item["Country"]: #task 3
    if True:
        for key in item:
        # for key in covid19_global.keys(): # task 4
            if key in titles:
                if key == 'Country':
                    if task == 4: continue
                    print("{0:<32s}".format(item[key]),end='')
                else:
                    print("{0:>20}".format(item[key]),end='')
                    # print("{0:>20}".format(covid19_global[key]),end='') # task 4
        print(end="\n")