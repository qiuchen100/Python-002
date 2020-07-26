#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import lxml.etree


def get_content():
    url = 'https://movie.douban.com/subject/1292052/'
    header = {}
    header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    resp = requests.get(url, headers=header)
    return resp.text


def parse_content(content):
    selector = lxml.etree.HTML(content)
    film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
    print(f'电影名称：{film_name[0]}')
    plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
    print(f'上映时间：{plan_date[0]}')
    rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
    print(f'评分：{rating[0]}')
    my_list = [film_name[0], plan_date[0], rating[0]]
    import pandas as pd
    movie1 = pd.DataFrame(data=my_list)
    movie1.to_csv('./movie1.csv', encoding='utf-8', index=False, header=False)


def main():
    content = get_content()
    parse_content(content)


if __name__ == "__main__":
    main()

