import requests
from datetime import datetime
import os
from time import sleep

success_file = open('files/success.log', 'a')
error_file = open('files/error.log', 'a')

while True:
    sleep(1)
    try: 
        TODAY = datetime.today().strftime("%d.%m.%Y")
        URL = f"https://api.privatbank.ua/p24api/exchange_rates?json&dates={TODAY}"

        response = requests.get(URL)
        # print(response.json())
        success_file.write(f'| {os.getlogin()} | {datetime.today().strftime("%d.%m.%Y %H:%M:%S")}\
        | {response.status_code} {response.reason} Operation success!\n')
    except:
        error_file.write(f'| {os.getlogin()} | {datetime.today().strftime("%d.%m.%Y %H:%M:%S")}\
        | {response.status_code} {response.reason} Operation failed!\n')
    # finally:
    #     success_file.close()
    #     error_file.close()
