import json


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


with open("files/file.json", 'w') as file:
    json.dump(data, file, indent=4, sort_keys=True, ensure_ascii=True)


obj = {"saleRateNB":15.6389750}

rez = json.dumps(obj, indent=2, ensure_ascii=True)
print(type(rez))

dat = json.loads(rez)
print(type(dat))


