#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_content():
    url = 'https://movie.douban.com/top250?start=0'
    header = {}
    header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    resp = requests.get(url, headers=header)
    return resp.text


def parse_content(content):
    content_parse_info = BeautifulSoup(content, 'html.parser')
    movies = content_parse_info.find_all('div', attrs={'class': 'hd'})
    for movie in movies:
        movie_infos = movie.find_all('a',)
        for movie_info in movie_infos:
            movie_href = movie_info.get('href')
            movie_title = movie_info.find('span', ).text
            print(f'链接: {movie_href}')
            print(f'名称: {movie_title}')


def main():
    content = get_content()
    parse_content(content)


if __name__ == "__main__":
    main()
