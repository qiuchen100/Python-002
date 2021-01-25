from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)

# 模拟不同的浏览器
print(f'chrome: {ua.chrome}')
# print(f'safari: {ua.safari}')
# print(f'ie: {ua.ie}')

# 模拟返回头部信息，推荐使用
print(f'random: {ua.random}')
