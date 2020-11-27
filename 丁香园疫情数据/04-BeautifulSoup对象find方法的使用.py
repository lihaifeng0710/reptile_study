#1.导入模块
from bs4 import  BeautifulSoup
#2.准备文档字符串
html='''略'''
#3.创建 BeautifulSoup对象
soup= BeautifulSoup(html,'lxml')
#4.查找title标签
title=soup.find('title')
print(title)
#5.查找a标签
a=soup.find('a')
print('a')

#根据属性进行查找
#查找id为link1的标签
#方式1；通过命名参数进行指定的
a=soup.find(id='link1')
print(a)
#方式2：通过attrs来指定属性字典，进行查找
a=soup.find(attrs={'id':'link1'})
print(a)

#根据文本内容进行查找
text=soup.find(text='Elsie')
print(text)

