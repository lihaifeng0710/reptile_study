#1.导入模块
import requests
#2.发送请求，获取响应
response=requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
#3.获取响应数据
# response.encoding="utf-8"
# print(response.text)
print(response.content.decode())