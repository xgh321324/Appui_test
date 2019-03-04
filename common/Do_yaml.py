#coding:utf-8
import yaml
import os

#获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
print(curPath)
#获取yaml路径
yamlpath = os.path.join(curPath, 'config')

#open方法直接读出来
with open(yamlpath,'r',encoding='utf-8') as f:
    cfg = f.read()
print(type(cfg))
print(cfg)

#用load方法转字典
d = yaml.load(cfg)
print(type(d))
print('d:',d)


