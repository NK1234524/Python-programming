import requests
url="https://www.bing.com/search?q=chat+gpt&form=ANNTH1&refig=68c9647654964c7dadb338ab9bc942a9&pc=U531&adppc=EDGEDBB"
print(requests.get(url))
print(requests.get(url).status_code)
#print(requests.get(url).text)