# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    intro = scrapy.Field()

    # def __str__(self):
    #     return f'|{self.item["title"]}|{self.item["link"]}|{self.item["intro"]}|\n\n'
