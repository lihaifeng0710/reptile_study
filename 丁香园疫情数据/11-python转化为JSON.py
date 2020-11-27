import json
#1.把python转化为JSON
json_str='''[{"id":4847256,"createTime":1596884703000,"modifyTime":1596884703000,"tags":"","countryType":2,"continents":"北美洲","provinceId":"8","provinceName":"美国","provinceShortName":"","cityName":"","currentConfirmedCount":3156780,"confirmedCount":4942008,"confirmedCountRank":1,"suspectedCount":0,"curedCount":1623870,"deadCount":161358,"deadCountRank":1,"deadRate":"3.26","deadRateRank":63,"comment":"","sort":0,"operator":"duchenjing","locationId":971002,"countryShortCode":"USA","countryFullName":"United States of America","statisticsData":"https://file1.dxycdn.com/2020/0315/553/3402160512808052518-135.json","incrVo":{"currentConfirmedIncr":15567,"confirmedIncr":15945,"curedIncr":0,"deadIncr":378},"showRank":true}]'''
rs=json.loads(json_str)
json_str=json.dumps(rs,ensure_ascii=False)
print(json_str)
#2.把python以JSON格式存储到文件中
with open('data/test1.json', 'w') as fp:
    json.dump(rs,fp,ensure_ascii=False)