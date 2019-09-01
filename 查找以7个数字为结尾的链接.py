from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://movie.douban.com/top250')
bs = BeautifulSoup(html.read(),'html.parser')

links = bs.find_all('a',{'href':re.compile('https:\/\/movie\.douban\.com\/subject\/.*')})
for link in links:
    print(link['href'])