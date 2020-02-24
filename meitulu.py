# -*- coding: utf-8 -*-
import scrapy
import re
from meitulu_project import items


class MeituluSpider(scrapy.Spider):
    name = 'meitulu'
    allowed_domains = ['meitulu.92demo.com']
    start_urls = [
        # 'http://meitulu.92demo.com/',
        'http://meitulu.92demo.com/t/yongzhuang/',
        'http://meitulu.92demo.com/t/keai/',
        'http://meitulu.92demo.com/t/ribenmeinv/',
        'http://meitulu.92demo.com/t/jipin/',
        'http://meitulu.92demo.com/t/tianmei/',
        'http://meitulu.92demo.com/t/qingchun/',
        'http://meitulu.92demo.com/t/duanfa/',
        'http://meitulu.92demo.com/t/mengmeizi/',
        'http://meitulu.92demo.com/t/shengyi/',
        'http://meitulu.92demo.com/t/jinjisheying/',
        'http://meitulu.92demo.com/t/qingxin/',
        'http://meitulu.92demo.com/t/xinggan/',
        'http://meitulu.92demo.com/t/zhifu/',
        'http://meitulu.92demo.com/t/xueshengmei/',
        'http://meitulu.92demo.com/t/shuishoufu/',
        'http://meitulu.92demo.com/t/SM/',
        'http://meitulu.92demo.com/t/jiemeihua/',
        'http://meitulu.92demo.com/t/mei/',
        'http://meitulu.92demo.com/t/baoru/',
        'http://meitulu.92demo.com/t/youhuo/',
        'http://meitulu.92demo.com/t/juru/'
    ]

    def parse(self, response):
        tag = response.xpath('/html/head/title/text()').getall()
        tag = tag[0][:4].strip('|')
        if not tag:
            tag = 'ERROR'
        page_links = response.xpath('//div[@class="boxs"]/ul[@class="img"]/li/a/@href').getall()
        cover_links = response.xpath('//div[@class="boxs"]/ul[@class="img"]/li/a/img/@src').getall()
        titles = response.xpath('//div[@class="boxs"]/ul[@class="img"]/li/a/img/@alt').getall()
        page_num = response.xpath('//div[@class="boxs"]/ul[@class="img"]/li/p/text()').getall()
        num = ''.join(page_num)
        pn = re.findall('[0-9]+张', num)
        fbl = re.findall('[0-9]+[x|X][0-9]+', num)
        print(pn, fbl)
        next_pages = response.xpath('//*[@id="pages"]/a/@href').getall()
        page_ids, a_links = [], []
        for page in page_links:
            url = 'http://meitulu.92demo.com' + page
            a_links.append(url)
            page_id = re.findall('[0-9]+', page)[0]
            page_ids.append(page_id)
        for i in range(len(page_links)):
            att = titles[i]
            aid = page_ids[i]
            aco = cover_links[i]
            aln = a_links[i]
            apn = pn[i]
            afb = fbl[i]
            item = items.MeituluProjectItem(class_tag=tag, article_title=att, article_id=aid, article_cover=aco,
                                            article_link=aln, article_num=apn, article_fbl=afb)
            yield item
        if next_pages:
            next_url = 'http://meitulu.92demo.com' + next_pages[-1]
            yield scrapy.Request(next_url, callback=self.parse)
        else:
            special_li = [f'http://meitulu.92demo.com/t/mengmeizi/index_{i}.html' for i in range(1, 37)]
            for url in special_li:
                yield scrapy.Request(url, callback=self.parse)
                special_li.remove(url)
