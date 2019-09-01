from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://movie.douban.com/top250')
bs = BeautifulSoup(html.read(),'html.parser')

images = bs.find_all('div',{'class':'title'})
for title in titleList:
    print(title.get_text())