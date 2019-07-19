# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:xia
@file: douban_spider.py
@time: 2019/7/19 12:17
"""


import requests
import json

class DoubanSpider(object):
    def __init__(self):
        self.start_url = "https://movie.douban.com/j/search_subjects?type=tv&tag=热门&sort=recommend&page_limit=20&page_start={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}


    def parse_url(self,url):
        response = requests.get(url,headers=self.headers)
        json_str = response.content.decode()
        return json_str

    def get_content_list(self,json_str):
        dict_ret = json.loads(json_str)
        return dict_ret["subjects"]

    def save_content_list(self,content_list):
        with open("douban.txt","a",encoding="utf-8") as f:
            for content in content_list:
                # ensure_ascii 默认不适用ascill编码，默认utf-8，如果没有该参数，中文以二进制写入文件
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")  # 换行符

    def run(self):
        num = 0
        while True:

            url = self.start_url.format(num)
            json_str = self.parse_url(url)
            context_list = self.get_content_list(json_str)
            if len(context_list) == 0:
                break
            self.save_content_list(context_list)
            num += 20


if __name__ == "__main__":
    douban = DoubanSpider()
    # run
    douban.run()