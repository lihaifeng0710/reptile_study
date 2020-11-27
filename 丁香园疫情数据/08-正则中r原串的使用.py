import re
# 不使用r原串

rs1=re.findall('a\nbc','a\nbc')
print(rs1)

rs2=re.findall('a\\nbc','a\\nbc')
print(rs2)

rs3=re.findall('a\\\nbc','a\\nbc')
print(rs3)

rs4=re.findall('a\\\\nbc','a\\nbc')
print(rs4)

#r原串可以消除转义符带来的影响
rs5=re.findall(r'a\\nbc','a\\nbc')
print(rs5)

