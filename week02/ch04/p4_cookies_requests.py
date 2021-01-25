import requests
from fake_useragent import UserAgent
from requests import cookies

ua = UserAgent(verify_ssl=False)
headers = {
    'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
    'User-Agent': ua.random
}

login_url = 'https://accounts.douban.com/j/mobile/login/basic'

form_data = {
    'ck': '',
    'name': '18665866991',
    'password': '8469375aaa',
    'remember': 'false',
    'ticket': ''}

# with requests.session() as s:

resp = requests.post(login_url, headers=headers, data=form_data)
print(resp.text)
print(resp.cookies)
setting_url = 'https://accounts.douban.com/passport/setting'
cookies = resp.cookies
resp = requests.get(setting_url, headers=headers, cookies=cookies)
print(resp.text)
print(resp.is_redirect)
