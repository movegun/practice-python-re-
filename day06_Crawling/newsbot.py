import scrapy


class NewsbotSpider(scrapy.Spider):
    name = 'newsbot'
    allowed_domains = ['news.naver.com']
    start_urls = ['http://news.naver.com/']

    def parse(self, response):
        pass
