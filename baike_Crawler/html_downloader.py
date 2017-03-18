#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/3/18 15:46
@Author  : CloudWind
@File    : html_downloader.py
@Version : Python 3.6.0
@Software: PyCharm
"""
from urllib import request


class HtmlDownloader(object):

    @staticmethod
    def download(url):
        if url is None:
            return None

        response = request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()
