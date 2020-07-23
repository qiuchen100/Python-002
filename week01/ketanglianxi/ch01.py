#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

def main():
    url = 'https://movie.douban.com/top250?start=0'
    header = {}
    header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    resp = requests.get(url, headers=header)
    print(f'内容是：{resp.text}')
    print(f'状态码是：{resp.status_code}')


if __name__ == "__main__":
    main()
