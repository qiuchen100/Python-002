import requests

r = requests.get('http://www.httpbin.org')
print(r.status_code)
print(r.headers)
