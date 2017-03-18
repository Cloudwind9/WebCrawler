#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/3/18 15:46
@Author  : CloudWind
@File    : html_parser.py
@Version : Python 3.6.0
@Software: PyCharm
"""
import re
from urllib import parse
from bs4 import BeautifulSoup


class HtmlParser(object):

    @staticmethod
    def _get_new_urls(page_url, soup):
        new_urls = set()
        # /view/123
        # links = soup.find_all('a', href=re.compile(r"/item/[a-z0-9A-Z%]+"))
        links = soup.find_all('a', href=re.compile(r"/item/[a-z0-9A-Z%]+"))
        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    @staticmethod
    def _get_new_data(page_url, soup):
        res_data = dict()

        # url
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title">
        # <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, "html.parser", from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
