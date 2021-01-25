import requests

# 模拟get
r = requests.get('https://gitee.com')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)

# 模拟post
r = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(r.json())
