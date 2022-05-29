import csv
from pprint import pprint

with open("files/file.csv", 'r', encoding='UTF8', newline='') as file:
    filereader = csv.DictReader(file, delimiter=',', quotechar='"')
    # print(filereader)
    for ind,  row in enumerate(filereader, 3):
        # if ind < 2: 
        #     continue
        print(ind, row)
        if ind == 1: 
            break
