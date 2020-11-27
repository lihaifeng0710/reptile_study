import requests
import os
url='http://img0.dili360.com/ga/M00/48/F7/wKgBy1llvmCAAQOVADC36j6n9bw622.tub.jpg'
root='E:\Pycharm-workspace\爬虫学习\慕课爬虫学习\image\\'
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已经存在')
except:
    print('爬取失败')

