# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json


class MeituluProjectPipeline(object):
    Res_Dir = 'E:/spider_download/meitulu/'
    if not os.path.isdir(Res_Dir):
        os.mkdir('E:/spider_download')
        os.mkdir(Res_Dir)

    def process_item(self, item, spider):
        with open('E:/spider_download/meitulu/' + f'{item.get("class_tag") +"_"+ item.get("article_id")}.json', 'w',
                  encoding='utf-8') as f:
            dic = {
                'class_tag': item.get("class_tag"),
                'article_title': item.get("article_title"),
                'article_id': item.get("article_id"),
                'article_cover': item.get("article_cover"),
                'article_link': item.get("article_link"),
                'article_pn': item.get("article_num"),
                'article_fbl': item.get("article_fbl")
            }
            json.dump(dic, f, ensure_ascii=False)
        pass
