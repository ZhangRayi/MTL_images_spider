# -*- coding: utf-8 -*-
from meitulu_image_project import items
import scrapy
import json
import os
import re


class MeituluImageSpider(scrapy.Spider):
    name = 'meitulu_image'
    allowed_domains = ['meitulu.92demo.com']
    urls = ['http://meitulu.92demo.com/item/3542.html']
    dir_path = 'E:/spider_download/meitulu/'
    file_list = os.listdir(dir_path)
    for file in file_list:
        with open(dir_path + file, 'r', encoding='utf-8') as f_IO:
            js = json.load(f_IO)
        urls.append(js['article_link'])
    start_urls = urls

    def parse(self, response):
        pic_link = response.xpath('//img[@class="content_img"]/@src').getall()
        current_name = response.xpath('//div[@class="weizhi"]/h1/text()').getall()[0]
        next_page = response.xpath('//div[@id="pages"]/a/@href').getall()
        next_link = 'http://meitulu.92demo.com' + next_page[-1]
        # num = response.xpath('//div[@class="c_l"]/p[3]').getall()[0]
        temp_p = re.findall('_[0-9]+', next_page[-1])
        # next_p = int(temp_p.strip('_'))
        print(temp_p)
        if len(temp_p) != 0:
            pic_name = current_name.replace('？', '').replace('*', '').replace('|', '').replace('！', '') \
                .replace('“', '').replace('<', '').replace('>', '').replace('：', '').replace('/', '')
            yield scrapy.Request(url=next_link, callback=self.parse)
            item = items.MeituluImageProjectItem(image_urls=pic_link, image_name=pic_name)
            yield item

        # else:
        #     sys.exit(f'{current_name} is finished')
        # print(pic_link, current_name, next_link)
        # yield pic_link, next_page
