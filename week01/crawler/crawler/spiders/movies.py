from urllib import parse
import scrapy
from bs4 import BeautifulSoup
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
        content_parse_info = BeautifulSoup(response.text, 'html.parser')
        movies = content_parse_info.find_all('div', attrs={'class': 'hd'})
        items = []
        for movie in movies:
            item = CrawlerItem()
            movie_info = movie.find('a',)
            title = movie_info.find('span', ).text
            link = movie_info.get('href')
            item['title'] = title
            item['link'] = link
            items.append(item)
        return items
