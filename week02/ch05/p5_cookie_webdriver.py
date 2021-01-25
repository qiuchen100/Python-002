from logging import exception
from requests import cookies
from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
    browser.get('http://www.douban.com')
    time.sleep(1)
    browser.switch_to_frame(browser.find_element_by_xpath(
        '//*[@id="anony-reg-new"]/div/div[1]/iframe'))
    btm1 = browser.find_element_by_xpath(
        '/html/body/div[1]/div[1]/ul[1]/li[2]')
    btm1.click()

    browser.find_element_by_xpath(
        '//*[@id="username"]').send_keys('18665866991')
    browser.find_element_by_xpath(
        '//*[@id="password"]').send_keys('8469375aaa')
    time.sleep(1)
    browser.find_element_by_xpath(
        '//a[contains(@class, "btn-account")]').click()

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)


except exception as e:
    print(e)
finally:
    browser.close()
