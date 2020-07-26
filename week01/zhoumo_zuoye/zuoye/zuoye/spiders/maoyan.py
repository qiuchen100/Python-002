import scrapy
from scrapy import Selector
from zuoye.items import ZuoyeItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        item = ZuoyeItem()
        movies = Selector(response).xpath(
            '//div[@class="movies-list"]/dl[@class="movie-list"]//div[@class="movie-hover-info"]')
        for movie in movies[:10]:
            film_name = movie.xpath(
                './div[@class="movie-hover-title"][1]/span[1]/text()').extract_first().strip()
            film_type = movie.xpath(
                './div[@class="movie-hover-title"][2]/text()').extract()[1].replace('\n', '').replace(' ', '')
            film_time = movie.xpath(
                './div[@class="movie-hover-title movie-hover-brief"]/text()').extract()[1].replace('\n', '').replace(' ', '')
            item['film_name'] = film_name
            item['film_type'] = film_type
            item['film_time'] = film_time
            yield item
