# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class ZuoyePipeline:
    def process_item(self, item, spider):
        movie = [item['film_name'], item['film_type'], item['film_time']]
        with open('./movies.csv', 'a+', encoding='utf-8') as fp:
            fp_csv = csv.writer(fp)
            fp_csv.writerow(movie)
        return item
