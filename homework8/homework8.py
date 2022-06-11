import requests

pages = []
for i in range(1, 6):
    url = "http://guba.eastmoney.com/list,zssh000001_?.html"
    url = url.replace("?", str(i))
    print(url)
    response = requests.get(url)
    html = response.text
    pages.append(html)