#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/3/18 15:47
@Author  : CloudWind
@File    : url_manager.py
@Version : Python 3.6.0
@Software: PyCharm
"""


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 未爬取过的URl队列
        self.old_urls = set()  # 爬取过的Url队列

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
