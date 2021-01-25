import requests
import os
from PIL import Image
import pytesseract

# 下载图片
# session = requests.session()
# img_url = 'https://images0.cnblogs.com/blog/508489/201505/101311124074020.png'
# agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
# headers = {'User-Agent': agent}
# r = session.get(img_url, headers=headers)

# with open('cap.png', 'wb') as f:
#     f.write(r.content)


# 打开并显示文件
im = Image.open('cap.png')
# im.show()

# 灰度化
gray = im.convert('L')
gray.save('cap_gray.png')
im.close()

# 二值化
threshold = 100
table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

out = gray.point(table, '1')
out.save('c_th.png')

th = Image.open('c_th.png')
print(pytesseract.image_to_string(th, lang='chi_sim+eng'))
th.close()
