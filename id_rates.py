import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":7.0337237217367e-5,"date":"Sun, 27 Dec 2020 00:00:01 GMT","inverseRate":14217.220345315},
             "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":5.7708232967066e-5,"date":"Sun, 27 Dec 2020 00:00:01 GMT","inverseRate":17328.54999339}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])