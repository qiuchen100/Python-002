import requests

# 在同一个Session实例发出的所有请求之间保持cookie
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)


# 上下文方式管理
with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/789456')
    r = s.get('http://httpbin.org/cookies')
    print(r.text)
