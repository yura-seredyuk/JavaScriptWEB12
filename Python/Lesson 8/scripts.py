"""
"""
import requests
import bs4
from datetime import datetime


def covid():
    URL = "https://api.covid19api.com/summary"
    img = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/1020px-SARS-CoV-2_without_background.png"
    data = """<i>Data</i>\n<i><b>COVID</b></i>"""
    response = requests.get(URL)
    results = list(filter(lambda x: x['Country'] == 'Ukraine', response.json()['Countries']))[0]
    data = f"""<i>Країна</i>: <b>{results["Country"]}</b>\n""" +\
            f"""<i>Нові випадки</i>: <b>{results["NewConfirmed"]}</b>\n""" +\
            f"""<i>Загальна кількість випадків</i>: <b>{results["TotalConfirmed"]}</b>\n""" +\
            f"""<i>Нових смертей</i>: <b>{results["NewDeaths"]}</b>\n""" +\
            f"""<i>Загальна кількість смертей</i>: <b>{results["TotalDeaths"]}</b>\n""" +\
            f"""<i>Нових одужань</i>: <b>{results["NewRecovered"]}</b>\n""" +\
            f"""<i>Загальна кількість одужань</i>: <b>{results["TotalRecovered"]}</b>\n"""
    print(data)
    return img, data

def weather():
    URL = "https://www.gismeteo.ua/ua/weather-rivne-4940/now/"
    img = "https://sinst.fwdcdn.com/img/newImg/sinoptic-logo.png"
    data = "<i><b>WEATHER</b></i>"
    return img, data


def courses():
    TODAY = datetime.today().strftime("%d.%m.%Y")
    URL = f"https://api.privatbank.ua/p24api/exchange_rates?json&dates={TODAY}"
    img = "https://play-lh.googleusercontent.com/smZQLdxpnc4YuKwRUwlellYbbC_HY13gMi9nlk5INAmzkQxSq6-g6HE96whLeX-uIA"
    data = "<i><b>Courses</b></i>"
    return img, data

def ork():
    img = "https://antikor.com.ua/foto/articles_foto/2022/03/30/533016.jpg"
    data = "<i><b>orks</b></i>"
    return img, data


if __name__ == "__main__":
    covid()
    pass
