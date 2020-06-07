# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:18:14 2020
invite code:j7hm
@author: fuwenyue 163密码： 4P2V2N9Z2f8F
"""
import requests,re,time

basedomain = 'https://freemycloud.cc'
my_proxies = {
    'http':'socks5://127.0.0.1:10808',
    'https':'socks5://127.0.0.1:10808'
    }

datalist = [
        {'email': '492119549@qq.com','passwd': '6N4eTlp6UxWQ','code':'', 'remember_me': 'on'},
        {'email': 'yoval@qq.com','passwd': 'dI86qBN4YjKp','code':'', 'remember_me': 'on'},
        {'email': 'yoval@foxmail.com','passwd': '4P2V2N9Z2f8F','code':'', 'remember_me': 'on'},
        {'email': '1505044520@qq.com','passwd': '6N4eTlp6UxWQ','code':'', 'remember_me': 'on'},
        {'email': 'webscraper@qq.com','passwd': 'dI86qBN4YjKp','code':'', 'remember_me': 'on'},
        {'email': 'webscraper@foxmail.com','passwd': 'dI86qBN4YjKp','code':'', 'remember_me': 'on'}
        ]
# 订阅链接
def DingyueUrl(code):
    # SSR 订阅
    SSRUrl = 'https://freemycloud.site/link/%s?sub=1'%code
    # ClashR 订阅
    ClashRurl = 'https://freemycloud.site/link/%s?clash=2'%code
    # SS 订阅 
    SSurl = 'https://freemycloud.site/link/%s?list=shadowrocket'%code
    # v2ray 订阅
    v2ray = 'https://freemycloud.site/link/%s?sub=3'%code
    return [SSRUrl,ClashRurl,SSurl,v2ray]

# 签到
def Check(datalist):
    C = input('请输入订阅类型（1：SSR:2：ClashR:3：SS:4：v2ray）：')
    if C=='1':
        print('您选择的类型为：SSR')
        C = 1
    elif C=='2':
        print('您选择的类型为：ClashR')
        C=2
    elif C=='3':
        print('您选择的类型为：SS')
        C=3
    elif C=='4':
        print('您选择的类型为：v2ray')
        C=4
    else:
        print('输入错误，默认为：SSR')
        C=3
        
    for data in datalist:
        conn = requests.session()
        rep = conn.post('%s/auth/login'%basedomain, data=data,proxies=my_proxies,timeout=5)
        repjson = rep.json()
        MSG = repjson['msg']
        print(MSG)
        if MSG == '登录成功':
            pass
        if MSG =='邮箱不存在':
            print('账号已被删除，跳过……')
            continue
        if MSG == '邮箱或者密码错误':
            print('请检查账号 %s 密码'%data['email'])
        # 签到
        checkrep = conn.post('%s/user/checkin'%basedomain,proxies=my_proxies,timeout=5)
        checkrepjson = checkrep.json()
        print(checkrepjson['msg'])
        #剩余流量
        htmlrep = conn.get('%s/user'%basedomain,proxies=my_proxies)
        liuliang = re.findall('<h4 class="m-b-0">(.*)</h4>', htmlrep.text)[2]
        print('此账号剩余流量：%s'%liuliang)
        dingyue = re.findall('data-clipboard-text="(.*)">复制',htmlrep.text)
        dingyue = list(set(dingyue))
        d = dingyue[0]
        Code = re.findall(r'link/(.*)\?',d)[0]
        DingyueUrlList = DingyueUrl(Code)
        print('订阅连接为：%s'%DingyueUrlList[C-1])

# 注册  
def REG(datalist):
    for data in datalist:
        print('正在尝试注册账号%s'%data['email'])  
        SENDdata = {'email': data['email']}
        print('正在尝试发邮件至:%s'%data['email'])
        SENDrep = requests.post('%s/auth/send'%basedomain,data = SENDdata,proxies=my_proxies)
        print(SENDrep.text)
        SENDjson = SENDrep.json()
        SENDmsg = SENDjson['msg']
        print(SENDmsg)
        if SENDmsg =='此邮箱已经注册':
            time.sleep(5)
            continue
        emailcode = input('请输入验证码：')
        REGdata = {
            'email': data['email'],
            'name': 'fuwenyue',
            'passwd': data['passwd'],
            'repasswd': data['passwd'],
            'code': 'j7m',
            'emailcode': emailcode,
        }
        REGrep = requests.post('%s/auth/register'%basedomain ,data = REGdata,timeout=5,proxies=my_proxies)
        REGjson = REGrep.json()
        MSG = REGjson['msg']
        print(MSG)

#测试代理
def CheckPorxy():
    IpUrl = 'https://ip.tour.pub/json'
    IPReq = requests.get(IpUrl)
    IPJson = IPReq.json()
    print('当前IP：%s，'%IPJson['ip'],'所在地区:%s'%IPJson['country'])
    try:
        IPReq = requests.get(IpUrl,proxies=my_proxies,timeout=5)
        IPJson = IPReq.json()
        print('当前代理IP为：%s，'%IPJson['ip'],'代理所在地区:%s'%IPJson['country'])
    except:
        print('代理连接错误')

CheckPorxy()
S = input('请输入运行模块（1.注册，2.签到）：')

if S =='1':
    REG(datalist)
else:
    Check(datalist)
    