# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:18:14 2020

@author: fuwenyue
"""
import requests,re

url = 'https://freemycloud.xyz/auth/login'
checkurl = 'https://freemycloud.xyz/user/checkin'
datalist = [
        {'email': '492119549@qq.com','passwd': '6N4eTlp6UxWQ','code':'', 'remember_me': 'on'},
        {'email': 'fuwenyue@outlook.com','passwd': 'Ofo9jK8Vt010','code':'', 'remember_me': 'on'},
        {'email': 'yoval@qq.com','passwd': 'dI86qBN4YjKp','code':'', 'remember_me': 'on'},
        {'email': 'fuwenyue77@gmail.com','passwd': '4HoNk0JrsbZS','code':'', 'remember_me': 'on'},
        {'email': 'yoval@foxmail.com','passwd': '4P2V2N9Z2f8F','code':'', 'remember_me': 'on'},
        ]
# 登录
for data in datalist:
    conn = requests.session()
    rep = conn.post(url, data=data)
    repjson = rep.json()
    print(repjson['msg'])
    # 签到
    checkrep = conn.post(checkurl)
    checkrepjson = checkrep.json()
    print(checkrepjson['msg'])
    #剩余流量
    htmlurl = 'https://freemycloud.xyz/user'
    htmlrep = conn.get(htmlurl)
    liuliang = re.findall('<h4 class="m-b-0">(.*)</h4>', htmlrep.text)[2]
    print('此账号剩余流量：%s'%liuliang)
'''
    dingyue = re.findall('data-clipboard-text="(.*)">复制',htmlrep.text)
    dingyue = list(set(dingyue))
    print('订阅地址：')
    for d in dingyue:
        print(d)
''' 