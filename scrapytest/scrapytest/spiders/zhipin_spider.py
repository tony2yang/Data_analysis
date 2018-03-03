#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 17:05
# @Author  : Tony
# @File    : zhipin_spider.py
__Author__ = 'Tony'

import scrapy
import time
from scrapytest.items import  ScrapytestItem


class ZhipinSpider(scrapy.Spider):
    name = 'zhipin'

    allowed_domains = ['www.zhipin.com']

    start_urls = ['http://www.zhipin.com/']

    positionUrl = 'https://www.zhipin.com/c101270100/h_101270100/?query=数据开发'
    curPage = 1

    # Request header
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'lastCity=101270100; JSESSIONID=""; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1519457432; __c=1519457459; __l=r=&l=%2Fwww.zhipin.com%2F; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1519457512; __a=56759131.1519457451.1519457451.1519457459.3.2.2.3',
        'Host': 'www.zhipin.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

    def start_requests(self):
        return [self.next_request()]

    def parse(self, response):
        print("request -> " + response.url)
        job_list = response.css('div.job-list > ul > li')
        for job in job_list:
            item = ScrapytestItem()
            job_primary = job.css('div.job-primary')
            item['pid'] = job.css('div.info-primary > h3 > a::attr(data-jobid)').extract_first().strip()
            item['positionName'] = job_primary.css('div.info-primary > h3 > a::text').extract_first().strip()

            yield item

        if self.curPage < 11:
            self.curPage += 1
            time.sleep(5)
            yield self.next_request()

    def next_request(self):
                return scrapy.http.FormRequest(
                    self.positionUrl + ("&page=%d&ka=page-%d" %
                                        (self.curPage, self.curPage)),
                    headers=self.headers,
                    callback=self.parse
                )