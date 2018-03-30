# coding=utf-8
from bs4 import BeautifulSoup
import urllib
import requests  
import time
"""
突破弹琴吧vip限制下载吉他谱
"""

def main(url):
    html = urllib.urlopen(url).read()
    #数据提取与清洗
    soup = BeautifulSoup(html,"html.parser")
    title = soup.h1.string
    img  =  soup.select('#img1')[0].img['src']
    urlImg = img.replace('image','web_image')

    count = 1
    while(get_status(urlImg)==200):
        filename = title+'_'+str(count)+'.png'
        downImg(urlImg,filename)
        urlImg = urlImg.replace(str(count)+'.png',str(count+1)+'.png')
        count = count + 1


#获取网页状态码
def get_status(url):  
    r = requests.get(url, allow_redirects = False)  
    return r.status_code 

#下载图片
def downImg(img,filename):
    data = urllib.urlopen(img).read()
    f = open(filename,'wb').write(data)


if __name__ == '__main__':
    #吉他谱地址
    url = "http://www.tan8.com/jitapu-55725.html"
    main(url)
