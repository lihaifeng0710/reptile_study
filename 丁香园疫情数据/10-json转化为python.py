import json
#1. json字符串转化为python数据
json_str='''[{"id":4847256,"createTime":1596884703000,"modifyTime":1596884703000,"tags":"","countryType":2,"continents":"北美洲","provinceId":"8","provinceName":"美国","provinceShortName":"","cityName":"","currentConfirmedCount":3156780,"confirmedCount":4942008,"confirmedCountRank":1,"suspectedCount":0,"curedCount":1623870,"deadCount":161358,"deadCountRank":1,"deadRate":"3.26","deadRateRank":63,"comment":"","sort":0,"operator":"duchenjing","locationId":971002,"countryShortCode":"USA","countryFullName":"United States of America","statisticsData":"https://file1.dxycdn.com/2020/0315/553/3402160512808052518-135.json","incrVo":{"currentConfirmedIncr":15567,"confirmedIncr":15945,"curedIncr":0,"deadIncr":378},"showRank":true}]'''
rs=json.loads(json_str)
print(rs)
print(type(rs))
print(type(rs[0]))
#2. 把json格式文件，转化为python类型的数据
with open('data/test.json') as fp:
    python_list=json.load(fp)
    print(python_list)
