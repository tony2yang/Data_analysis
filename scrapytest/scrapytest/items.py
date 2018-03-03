# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#define scrapy items

import scrapy


class ScrapytestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pid = scrapy.Field()
    positionName = scrapy.Field()
    positionLables = scrapy.Field()
    workYear = scrapy.Field()
    salary = scrapy.Field()
    city = scrapy.Field()
    education = scrapy.Field()
    companyShortName = scrapy.Field()
    industryField = scrapy.Field()
    financeStage = scrapy.Field()
    companySize = scrapy.Field()
    time = scrapy.Field()
    updated_at = scrapy.Field()
