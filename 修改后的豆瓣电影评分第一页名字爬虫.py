from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://movie.douban.com/top250')
bs = BeautifulSoup(html.read(),'html.parser')

titleList = bs.find_all('span',{'class':'title'})
for title in titleList:
    print(title.get_text())