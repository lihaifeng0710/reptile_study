# 导入正则模块
import re

#字符匹配
rs1=re.findall('abc','abcggjgygabc')
rs2=re.findall('a.c','a\nc')
rs3=re.findall('a.c','abc')
rs4=re.findall('a\.c','a.c')
rs5=re.findall('a[bc]d','abd')
print(rs1)
print(rs2)
print(rs3)
print(rs4)
print(rs5)

#预定义的字符集
rs6=re.findall('\d','123')
rs7=re.findall('\w','Az758_你好')
print(rs6)
print(rs7)

#数量词
rs8=re.findall('a\d*','a123')
print(rs8)
rs9=re.findall('a\d+','a1')
print(rs9)
rs10=re.findall('a\d?','a123')
print(rs10)
rs11=re.findall('a\d{2]','a123')
print(rs11)