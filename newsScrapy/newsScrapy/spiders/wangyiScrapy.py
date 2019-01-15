#scrapy crawl wangyiScrapy -a allowed_domains=news.163.com -a start_urls=https://news.163.com/
# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import scrapy
from es import ElasticObj 

class WangyiscrapySpider(scrapy.Spider):
    name = 'wangyiScrapy'
    scrapyed_urls_set = {};
    to_scrapy_urls_set = {};
    es_obj = ElasticObj()

    def __init__(self, allowed_domains=None, start_urls=None, *args, **kwargs):
        super(WangyiscrapySpider, self).__init__(*args, **kwargs)
        self.allowed_domains = [allowed_domains]#['news.163.com']
        self.start_urls = [start_urls]#['https://news.163.com/']

    #custom_settings = {
    #    "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    #}

    def parse(self, response):
        if self.scrapyed_urls_set.has_key(response.url) == False:
            self.scrapyed_urls_set[response.url] = 1
        if self.to_scrapy_urls_set.has_key(response.url) == True:
            self.to_scrapy_urls_set.pop(response.url)
        #json = "{'url' : "+response.url+",'html': "+response.body.decode('gbk')+"}";
        #print(json)
        self.es_obj.insert(response.url, response.body.decode('gbk'));

        urls = response.xpath('//a/@href').extract()
        for i in range(0, len(urls)):
            if urls[i].find(self.allowed_domains[0]) != -1:
                if self.scrapyed_urls_set.has_key(urls[i]) == False and self.to_scrapy_urls_set.has_key(urls[i]) == False:
                    self.to_scrapy_urls_set[urls[i]] = 1
                    print urls[i]
                    #if urls[i].find(".html") != -1 or urls[i].find(".htm") != -1:
                    #    print response.body.decode('gbk')
        
        yield scrapy.Request(url = self.to_scrapy_urls_set.keys()[0],callback = self.parse)

        #print urls
        pass


