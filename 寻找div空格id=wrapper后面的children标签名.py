from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://movie.douban.com/top250')
bs = BeautifulSoup(html,'html.parser')

for child in bs.find('div',{'id':'wrapper'}).children:
    print(child)