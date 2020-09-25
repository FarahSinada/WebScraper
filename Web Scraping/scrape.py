import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
print(res)
# grab the data only, don't need styling info
# print(res.text)