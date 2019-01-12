# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import scrapy


class WangyiscrapySpider(scrapy.Spider):
    name = 'wangyiScrapy'
    allowed_domains = ['news.163.com']
    start_urls = ['https://news.163.com/']
    #custom_settings = {
    #    "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    #}

    def parse(self, response):
        urls = response.xpath('//a/@href').extract()
        for i in range(0, len(urls)):
            if urls[i].find(self.allowed_domains[0]) != -1:
                print urls[i]
                if urls[i].find(".html") != -1 or urls[i].find(".htm") != -1:
                    print response.body.decode('gbk')
                yield scrapy.Request(url = urls[i],callback = self.parse)

        #print urls
        pass


