#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/3/18 13:54
@Author  : CloudWind
@File    : myUrllibCase.py
@Version : Python 3.6.0
@Software: PyCharm
"""

import urllib.request
import http.cookiejar

url = "http://baike.baidu.com/item/Python"

print("第一种方法")
response1 = urllib.request.urlopen(url)  # 直接请求
print(response1.getcode())  # 获取状态吗 如果是200表示成功
print(len(response1.read()))  # 读取内容长度

print("第二种方法")
request = urllib.request.Request(url)  # 创建Request对象
request.add_header('User-Agent', 'Mozilla/5.0')  # 添加http的header
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print("第三种方法")
cj = http.cookiejar.CookieJar()  # 创建cookie容器
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))  # 创建1个opener
urllib.request.install_opener(opener)  # 给urllib安装opener
response3 = urllib.request.urlopen(url)  # 使用带有cookie的urllib访问网络
print(response3.getcode())
print(cj)  # 打印cookie
print(response3.read())  # 打印网页的内容
