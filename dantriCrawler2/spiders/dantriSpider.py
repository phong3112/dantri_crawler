# -*- coding: utf-8 -*-                                                                                                                                                
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from dantriCrawler2.items import Dantricrawler2Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

#import pudb; pudb.set_trace()                                                                                                                                          
class dantriSpider(CrawlSpider):
    name = "dantri_crawl"
    allowed_domains = ["dantri.com.vn"]
    start_urls = ["http://dantri.com.vn"]

    rules = [
        Rule(LinkExtractor(allow=('(http://dantri.com.vn)')), callback = 'parse', follow = True),
        Rule(LinkExtractor(allow=('(.*\/.*\.htm)')), callback = 'parse_top_menu', follow=True),
        Rule(LinkExtractor(allow=('(.*\/.*\/([a-z]*-)*\d*\.htm)'), deny=('(.*\/.*\/trang-\d\.htm)')), callback = 'parse_dir_contents', follow=True),
    ]
    def parse(self, response):
        for top_url in response.xpath('//ul[@class="nav"]/li/a/@href').extract()[1:]:
            url = response.urljoin(top_url)
            yield scrapy.Request(url, callback=self.parse_top_menu)

    def parse_top_menu(self, response):
        for sel in Selector(response).xpath('//div[@class="clearfix"]/div[@class="mt3 clearfix"]/div[@class="mr1"]/h2'):
            link = sel.xpath("a/@href").extract()[0]
            if link:
		url = response.urljoin(link)
                yield scrapy.Request(url, callback=self.parse_dir_contents)

        next_page = response.xpath('//div[@class="fr"]/a/@href').extract()
        if next_page:
            link = next_page[0]
            url = response.urljoin(link)
            yield scrapy.Request(url, callback=self.parse_top_menu)
        else:
            return

    def parse_dir_contents(self, response):
        item = Dantricrawler2Item()
        item["title"] = response.xpath('//h1[@class="fon31 mgb15"]/text()').extract()

        ori_url = response.xpath('//link[@rel="canonical"]/@href').extract()
        if ori_url:
            item["link"] = ori_url[0]

        item["content"] = []
        for p_tag in response.xpath('//div[@class="fon34 mt3 mr2 fon43 detail-content"]/p/text()'):
            item["content"].append(p_tag.extract().strip())
            # print p_tag.extract()                                                                                                                                     
            # output.append(p_tag.extract().strip())                                                                                                                    
        yield item

