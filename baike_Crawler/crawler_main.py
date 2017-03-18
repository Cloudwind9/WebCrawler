#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/3/18 15:46
@Author  : CloudWind
@File    : crawler_main.py
@Version : Python 3.6.0
@Software: PyCharm
"""
from baike_Crawler import html_downloader
from baike_Crawler import html_outputer
from baike_Crawler import html_parser
from baike_Crawler import url_manager


class CrawlerMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, my_root_url):
        count = 1  # 记录查询的第几个URL
        self.urls.add_new_url(my_root_url)
        while self.urls.has_new_url():
            # noinspection PyBroadException
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 10:
                    break

                count += 1
            except Exception as e:
                print(e)

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = "http://baike.baidu.com/item/Python"
    obj_crawler = CrawlerMain()
    obj_crawler.craw(root_url)
