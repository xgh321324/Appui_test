# coding:utf-8
import time,datetime,os
import unittest
import HTMLTestRunner
from common.Send_email import Send_email


#from BeautifulReport import BeautifulReport
def all_case():
    '''
    .discover 方法里面有三个参数：
    -case_dir:这个是待执行用例的目录。
    -pattern：这个是匹配脚本名称的规则，test*.py 意思是匹配 test 开头的所有脚本。
    -top_level_dir：这个是顶层目录的名称，一般默认等于 None 就行了
    '''
    #待执行的测试用例
    case_dir = 'C:\\Users\\Administrator\\Documents\\GitHub\\LanTin\\case'
    test_case = unittest.TestSuite()   #创建测试套件(此时是个空的)
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py', top_level_dir=None)
    #将discover筛选出的测试用例循环添加到测试套件中
    for case in discover:
        test_case.addTest(case)
    print(test_case)
    '''
    for case in discover:
        for i in case:
            test_case.addTest(i)
    '''
    return test_case


if __name__ == '__main__':
    #be_run=unittest.TextTestRunner() #返回实例
    #run所有用例
    #be_run.run(all_case())
    now_time = time.strftime('%Y_%m_%d %H_%M_%S',time.localtime())
    #报告存放路径,若用HTMLTestRunner则要加上具体文件名称
    report_path = ("C:\\Users\\Administrator\\Documents\\GitHub\\LanTin\\report\\" + now_time + ".html")
    today = datetime.date.today()

    with open(report_path,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
                stream=f,
                title='澜渟app测试',
                description='这是'+str(today)+'日的测试结果',
                verbosity=2
        )
        runner.run(all_case())#这种用法也不错，也挺好看

    Send_email('15651797525@163.com',
               '15651797525@163.com',
               'xgh321324',
               ['15651797525@163.com','15651797525@139.com','970185127@qq.com']
               ,report_path).send()  #xgh321324是授权码登录
    print('发送成功！')
