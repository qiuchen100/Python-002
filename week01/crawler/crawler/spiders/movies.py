from urllib import parse
import scrapy
from bs4 import BeautifulSoup
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
        soup = BeautifulSoup(response.text, 'html.parser')
        movies = soup.find_all('div', attrs={'class': 'hd'})
        for movie in movies:
            item = CrawlerItem()
            movie_info = movie.find('a',)
            title = movie_info.find('span', ).text
            link = movie_info.get('href')
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        intro = soup.select('div.related-info')[0].get_text().strip()
        item['intro'] = intro
        yield item
