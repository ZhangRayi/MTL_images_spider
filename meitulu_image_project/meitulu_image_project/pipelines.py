# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
import re
from scrapy.pipelines.images import ImagesPipeline
from urllib.parse import urlparse


class MeituluImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            # "Cache-Control": "no-cache",
            # "Connection": "keep-alive",
            # "Host": "img.92demo.com:8010",
            # "Pragma": "no-cache",
            'Referer': 'http://meitulu.92demo.com/item/3542_93.html',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.17 Safari/537.36 Edg/81.0.416.11"
        }
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url,
                                 headers=headers,
                                 # meta={'name': item['image_name']},
                                 # callback=self.file_path
                                 )
            pass
        return item

    def file_path(self, request, response=None, info=None):
        par = urlparse(request.url).path
        name = re.findall('[0-9]+.jpg', par)[0]
        filename = os.path.basename(name)
        image_guid = filename.strip('.jpg')
        return 'full/%s.jpg' % image_guid
