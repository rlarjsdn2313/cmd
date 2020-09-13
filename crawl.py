from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import os


def crawling(cmd, d):
    baseUrl = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query='
    plusUrl = cmd[11:]
    url = baseUrl + quote_plus(plusUrl)

    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    img = soup.find_all(class_='_img')

    d= int(d)
    path = os.getcwd()
    n = 1
    for i in img:
        
        imgUrl = i['data-source']
        with urlopen(imgUrl) as f:
            if not os.path.exists(plusUrl):
                os.makedirs(plusUrl)
            with open(path + '//' + 'image' + "//" + plusUrl + "//" + plusUrl + str(n) + '.jpg', 'wb') as h:
                img = f.read()
                h.write(img)
        n += 1
        print(i)
        if n == d + 1:
            hdd = 'done'
            return hdd

