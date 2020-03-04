import requests
from bs4 import BeautifulSoup
import re
import time
chapter=[]
title=[]
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
def getUrl(Url):
    r=requests.get(Url,headers=headers)
    r.encoding='gbk'
    return r.text
def getHead(html):
    soup=BeautifulSoup(html,"html.parser")
    head=soup.title.string
    chapters=soup.find_all(href=re.compile("html"))
    for chapter1 in chapters[1:]:
        chapter.append(chapter1.text)
        title.append('https://www.230book.com/book/7709/'+chapter1.get('href'))
    datalist=dict(zip(title,chapter))
    return datalist,title,chapter
def getData(i):     #获取网页内容
    # for i in datalist.keys():
    soup=BeautifulSoup(getUrl(i))
    contents=soup.find_all(id="content")
    for content in contents:
        saveTxt(content.text.replace(u'\xa0',u''))
    saveTxt('\n')


def saveTxt(contents):
    with open("腾飞航空.txt",mode='a') as fp:
        fp.write(contents)

if  __name__=="__main__":
    c,a,b=getHead(getUrl('https://www.230book.com/book/7709/'))
    # for i in list(c.keys())[1:]:
        # saveTxt(c[i] + '\n')
        # getData(i)

    for i in a[397:]:
        saveTxt(c[i]+'\n')
        getData(i)




