# coding=utf-8
from base64 import encode
import datetime
import time

import json5
import requests

# 116.924525, 31.815721
# 116.917976764514,31.809860673369
secrets = json5.load(open('./.secret.json', 'r'))
dizhi = secrets['dizhi']
params = {'key': secrets['myhfkey'], 'location': str(dizhi[1]) + ',' + str(dizhi[0]), 'lang': 'zh'}
weather_api = "https://devapi.qweather.com/v7/weather/24h"
wechat_api = "https://sctapi.ftqq.com/SCT177773TTTMeLxiYA8W1ZwRZcvL533N8.send"
# print(params)
x = requests.get(weather_api, params=params)
weatherinfo = json5.loads(x.text)

file = open('./a.json', 'w', encoding='utf-8')
file.write(x.text)

# precipitation_marker = 0
# for a in weatherinfo['result']['minutely']['probability']:
#     if a != 0:
#         precipitation_marker = 1

# # 测试
# precipitation_marker = 1
# if precipitation_marker:
#     with open('./data.json') as f:
#         try:
#             data_data = json5.load(f)
#         except:
#             data_data = {'last_send_data': "2019-06-30 09:58:02"}
#     last_send_data = data_data['last_send_data']
#     last_send_data = time.mktime(time.strptime(
#         last_send_data, "%Y-%m-%d %H:%M:%S"))
#     now_time = time.mktime(time.strptime(
#         datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"))
#     if last_send_data < now_time:
#         precipitation_2h = weatherinfo['result']['minutely']['precipitation_2h']
#         data = {
#             "text": u"天气预警！",
#             "desp": weatherinfo['result']['forecast_keypoint']
#         }
#         req = requests.post(wechat_api, data=data)
#         datajson = {"last_send_data": (datetime.datetime.now(
#         )+datetime.timedelta(hours=4)).strftime("%Y-%m-%d %H:%M:%S")}
#         # print(datajson)
#         json5.dump(datajson, open('./data.json', 'w'))
