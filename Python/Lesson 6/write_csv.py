import csv

data = {
        "exchangeRate":
        [
            {"baseCurrency":"UAH","currency":"CHF","saleRateNB":15.6389750,"purchaseRateNB":15.6389750,"saleRate":17.0000000,"purchaseRate":15.5000000},
            {"baseCurrency":"UAH","currency":"EUR","saleRateNB":18.7949200,"purchaseRateNB":18.7949200,"saleRate":20.0000000,"purchaseRate":19.2000000},
            {"baseCurrency":"UAH","currency":"GBP","saleRateNB":23.6324910,"purchaseRateNB":23.6324910,"saleRate":25.8000000,"purchaseRate":24.0000000},
            {"baseCurrency":"UAH","currency":"PLZ","saleRateNB":4.4922010,"purchaseRateNB":4.4922010,"saleRate":5.0000000,"purchaseRate":4.2000000},
            {"baseCurrency":"UAH","currency":"USD","saleRateNB":15.0564130,"purchaseRateNB":15.0564130,"saleRate":15.7000000,"purchaseRate":15.3500000},
            {"baseCurrency":"UAH","currency":"CAD","saleRateNB":13.2107400,"purchaseRateNB":13.2107400,"saleRate":15.0000000,"purchaseRate":13.0000000}
        ]
    }

header = ["baseCurrency", "currency", "saleRateNB", "purchaseRateNB", "saleRate", "purchaseRate"]
# header = list(data["exchangeRate"][0].keys())

# print(header)

# file = open("files/file.csv", 'w', encoding='UTF8', newline='')
# writer = csv.writer(file, delimiter=',')
# writer.writerow(header)
# writer.writerows(data["exchangeRate"])
# file.close()

with open("files/file.csv", 'w', encoding='UTF8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC,)
    writer.writeheader()
    writer.writerows(data["exchangeRate"])