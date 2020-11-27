import re
#1. findall方法，返回匹配的结果列表
rs1=re.findall('\d','chun13zhi24')
print(rs1)

#2. findall方法中，flag参数的作用
rs2=re.findall('a.bc','a\nbc',re.S)
print(rs2)

#3.findall方法中分组的使用
rs3=re.findall('a.+bc','a\nbc',re.S)
print(rs3)

rs4=re.findall('a(.+)bc','a\nbc',re.S)
print(rs4)