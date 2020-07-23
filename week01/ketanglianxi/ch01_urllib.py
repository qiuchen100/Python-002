#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import request

def main():
    url = 'https://movie.douban.com/top250?start=0'
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36')
    with request.urlopen(req) as resp:
        print(f'内容是：{resp.read().decode("utf-8")}')
        print(f'状态码是：{resp.status}')

if __name__ == "__main__":
    main()