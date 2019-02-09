#scrapy crawl wangyiScrapy -a allowed_domains=news.163.com -a start_urls=https://news.163.com/
#/usr/local/python3.5.1.jun/bin/python3 -m scrapy crawl wangyiScrapy -a allowed_domains=news.163.com -a start_urls=https://news.163.com/
# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule

import scrapy
from es import ElasticObj 
from lxml import etree

from UrlObject import UrlObject
from scrapy.selector import Selector


from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

class WangyiscrapySpider(scrapy.Spider):
    name = 'wangyiScrapy'
    handle_httpstatus_list = [404, 301]
    es_obj = ElasticObj()
    url_object = UrlObject()

    def __init__(self, allowed_domains=None, start_urls=None, *args, **kwargs):
        super(WangyiscrapySpider, self).__init__(*args, **kwargs)
        self.allowed_domains = [allowed_domains]#['news.163.com']
        self.start_urls = [start_urls]#['https://news.163.com/']

    #custom_settings = {
    #    "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    #}

    def parse(self, response):
        if response.url.find(".htm") != -1:
            self.url_object.scrapyed(response.url);
            self.parse_html_and_insert_to_es(response)

        urls = response.xpath('//a/@href').extract()
        for i in range(0, len(urls)):
            if urls[i].find(self.allowed_domains[0]) != -1:
                self.url_object.toScrapyed(urls[i])
      
        nextUrl = self.url_object.getNextUrl();
        yield scrapy.Request(url = nextUrl, callback = self.parse, dont_filter = True)

    def parse_html_and_insert_to_es(self, response):
        selector = Selector(response)
        title = selector.xpath('//*[@id="epContentLeft"]/h1/text()')
        if title:
            title = title[0].xpath('string(.)')
        content = selector.xpath('//*[@id="endText"]')

        if content:
            content = content[0].xpath('string(.)').extract()[0]

        #title = soup.select("#epContentLeft > h1")
        #content = soup.select("#endText")
    
        #print(response.url)
        #print(title)
        #print(content)
        self.es_obj.insert(response.url, title, content);


