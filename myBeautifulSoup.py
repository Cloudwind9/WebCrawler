#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/3/18 14:27
@Author  : CloudWind
@File    : myBeautifulSoup.py
@Version : Python 3.6.0
@Software: PyCharm
"""

from bs4 import BeautifulSoup
import re  # 导入正则表达式

from urllib import request

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/item/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/item/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/item/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

"""
# 根据HTML网页字符串创建BeautifulSoup对象
soup = BeautifulSoup(html_doc,  # HTML文档字符串
                     'html.parser',  # HTML解析器
                     from_encoding='utf-8'  # HTML文档的编码
                     )
print("获取所有的链接")
# 查找所有标签为a的节点
# soup.find_all('a', href='/view/123.html')
# soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
links = soup.find_all('a')
for link in links:
    print(link.name,  # 获取查找到的节点的标签名称
          link['href'],  # 获取查找到的节点的href属性
          link.get_text())  # 获取查找到的节点的链接文字

# 查找所有标签为div, class为abc, 文字为Python的节点
# soup.find_all('div', class_='abc', string='Python')

print("获取Lacie的链接")
link_node = soup.find('a', href='http://example.com/item/lacie')
print(link_node.name, link_node['href'], link_node.get_text())

print("正则匹配")
regular_nodes = soup.find_all('a', href=re.compile(r"/item/[a-z0-9A-Z%]+"))
for regular_node in regular_nodes:
    print(regular_node.name, regular_node['href'], regular_node.get_text())

print("获取<p>段落文字")
p_node = soup.find('p', class_="title")
print(p_node.name, p_node.get_text())
"""

response = request.urlopen("http://baike.baidu.com/item/Python")
soup = BeautifulSoup(response.read(), 'html_parser', from_encoding='utf-8')
title = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
print(title)
