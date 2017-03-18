#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/3/18 15:47
@Author  : CloudWind
@File    : html_outputer.py
@Version : Python 3.6.0
@Software: PyCharm
"""


class HtmlOutputer(object):
    def __init__(self):
        self.data = []

    def collect_data(self, data):
        if data is None:
            return
        self.data.append(data)

    def output_html(self):
        fout = open("output.html", 'w', encoding='UTF-8')

        fout.write('<html>')
        fout.write('<head><meta charset="utf-8"></head>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.data:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()
