# coding:utf-8
from bs4 import BeautifulSoup
import requests
import time
import os
# 导入tomorrow
from tomorrow import threads

# 当前脚本所在目录
cur_path = os.path.dirname(os.path.realpath(__file__))

def get_image():
    r = requests.get('http://699pic.com/sousuo-218808-13-1.html')
    f = r.content
    soup = BeautifulSoup(f,'html.parser')
    # 找出所有标签
    image = soup.find_all(class_='lazy')
    return image

# 用法简单，只要在需要执行多线程的函数前加上此装饰器即可
@threads(5)
def save_image(image_url):
    try:
        jpg_url = image_url['data-original']
        title = image_url['title']
        '''
        # 判断是否有jpg文件夹，没有就创建一个
        save_file = os.path.join(cur_path,'jpg_haha')
        if not os.path.exists(save_file):
            os.mkdir(save_file)
        '''
        with open(r'F:\pic3\\'+title+'.jpg','wb') as fa:
            fa.write(requests.get(jpg_url).content)
    except Exception as e:
        pass

if __name__=='__main__':
    t1 = time.time()
    image_urls = get_image()
    for i in image_urls:
        save_image(i)
    t2 = time.time()
    print('总耗时：%.2f 秒' % (t2-t1))  # 取小数点后2位



