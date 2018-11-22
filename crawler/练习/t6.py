from bs4 import BeautifulSoup
from bs4.element import Tag
import re

with open(r'C:\Users\Administrator\Desktop\Python网络班学习资料\02-Python配套PPT\26Python-爬虫\test.html',encoding='utf-8') as res:
    soup = BeautifulSoup(res,'lxml')

    print(soup.select('[src$="com/"]'))
    print(2, soup.select('.title'))
    # 使用了伪类
    print(3, soup.select('div.content > p:nth-of-type(2)'))  # 同标签名p的第2个，伪类只实现了nth-of - type，且要求是数字
    # id选择器
    print(4, soup.select('p#second'))
    print(5, soup.select('#bg1'))
    # 后代选择器
    print(6, soup.select('div p'))  # div下逐层找p
    print(7, soup.select('div div p'))  # div下逐层找div下逐层找p
    # 子选择器，直接后代
    print(8, soup.select('div > p')[0].string)  # div下直接子标签的p
    # 相邻兄弟选择器
    print(9, soup.select('div p:nth-of-type(1) + [src]'))  # 返回[]
    # 普通兄弟选择器
    print(10, soup.select('div p:nth-of-type(1) ~ [src]'))
    # 属性选择器
    print(11, soup.select('[src]'))  # 有属性src
    print(12, soup.select('[src="/"]'))  # 属性src等于/
    print(13, soup.select('[src="http://www.magedu.com/"]'))  # 完全匹配
    print(14, soup.select('[src^="http://www"]'))  # 以http://www开头
    print(15, soup.select('[src$="com/"]'))  # 以com/结尾
    print(16, soup.select('img[src*="magedu"]'))  # 包含magedu
    print(17, soup.select('img[src*=".com"]'))  # 包含.com
    print(18, soup.select('[class~=title]'))  # 多值属性中有一个title