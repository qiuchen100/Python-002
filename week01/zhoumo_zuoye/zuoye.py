#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv


def get_content():
    url = 'https://maoyan.com/films?showType=3&sortId=1'
    header = {}
    header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    header[
        'Cookie'] = 'uuid_n_v=v1; uuid=16669340CF1711EA9BFE43BA456BAEDEF1E5F33818F84BFDBCF14504D7155F9F; _csrf=bb75e2cfdb66afa606983c9b19c7d4f40c2ce0ba5c32fb0a701f46dc01e18992; mojo-uuid=d7101a4603827f72ae1eb7106e5b8e6e; _lxsdk_cuid=1738a29ddadc8-02e31f3ba815408-491b3601-13c680-1738a29ddadc8; _lxsdk=16669340CF1711EA9BFE43BA456BAEDEF1E5F33818F84BFDBCF14504D7155F9F; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595750866,1595753987; mojo-session-id={"id":"74dd8d0846f031922a491c90357d3eca","time":1595647316093}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595647327; __mta=150247945.1595499635438.1595647316257.1595647327282.8; _lxsdk_s=17383fdccb9-41c-848-528%7C%7C6'
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',  # noqa: E501
               'Connection': 'keep-alive',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    resp = requests.get(url, headers=header)
    return resp.text


def parse_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    movies = soup.find_all('div', attrs={'class': 'movie-hover-info'})
    for movie in movies[:10]:
        movie_info_list = movie.find_all(
            'div', attrs={'class': 'movie-hover-title'})
        film_name = movie_info_list[0].find('span', ).text
        film_type = movie_info_list[1].text.replace('\n', '').replace(' ', '')
        film_time = movie_info_list[3].text.replace('\n', '').replace(' ', '')
        print(film_name + " || " + film_type + " || " + film_time)
        with open('./movies.csv', 'a+', encoding='utf-8') as fp:
            fp_csv = csv.writer(fp)
            fp_csv.writerow([film_name, film_type, film_time])


def main():
    content = get_content()
    parse_content(content)


if __name__ == "__main__":
    main()
