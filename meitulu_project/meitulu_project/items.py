# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeituluProjectItem(scrapy.Item):
    # define the fields for your item here like:
    class_tag = scrapy.Field()       # 当前内容是什么类型
    article_title = scrapy.Field()   # 内容的标题
    article_id = scrapy.Field()      # 内容的id
    article_cover = scrapy.Field()   # 内容的封面
    article_link = scrapy.Field()    # 内容的具体链接，通过此链接获取所有的大分辨率图片
    article_num = scrapy.Field()     # 内容共有多少图片
    article_fbl = scrapy.Field()     # 内容中图片的分辨率
    pass
