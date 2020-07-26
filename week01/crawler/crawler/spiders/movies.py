from urllib import parse
import scrapy
from scrapy import Selector
from crawler.items import CrawlerItem


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def start_requests(self):
        items_per_page = 25
        urls = tuple(
            f'{self.start_urls[0]}?start={items_per_page * page}' for page in range(10))
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        movies = Selector(response).xpath('//div[@class="hd"]')
        for movie in movies:
            item = CrawlerItem()
            title = movie.xpath('./a/span/text()').extract_first().strip()
            link = movie.xpath('./a/@href').extract_first().strip()
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        intro = Selector(response).xpath(
            '//div[@class="related-info"]').extract_first().strip()
        item['intro'] = intro
        yield item
