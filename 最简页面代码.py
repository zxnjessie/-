from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://movie.douban.com/top250')
bs = BeautifulSoup(html.read(),'html.parser')



print(bs.h1)