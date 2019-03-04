#coding:utf-8
import time,smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart  #发送附件用的

class Send_email():
    '''
    这个模块写的是可被调用的发送邮件的模块
    '''
    def __init__(self,sender,username,password,receivers,file_dir):
        #file_dir是绝对路劲 授权码: xgh321324  qq邮箱授权码：yagcogxporkmbcac
        self.sender = sender
        self.username = username
        self.password = password
        self.receivers = receivers
        self.file_dir = file_dir

    def send(self):
        with open(self.file_dir,'rb') as f:
            mail_body = f.read()
        server = 'smtp.163.com'
        subject = '这是今天的测试报告'
        #msg = MIMEText(body,_subtype='html',_charset='utf-8')   #html和utf-8容易忘了加引号，这里要注意

        '''定义邮件内容'''
        msg = MIMEMultipart()
        msg['subject'] = Header(subject)
        msg['From:'] = self.sender
        msg['To:'] = ','.join(self.receivers)
        body = MIMEText(mail_body,_subtype='html',_charset='utf-8')
        msg.attach(body)  #添加正文

        '''附件'''
        att = MIMEText(mail_body,'base64','utf-8')
        att['Content-type']="application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="my_report.html"' #附件重命名字
        msg.attach(att)#添加附件
        #上面这一部分好像必须是这个格式，不然会报错吧

        '''发送邮件'''
        smtp = smtplib.SMTP(server,25)
        smtp.connect('smtp.163.com')
        smtp.login(self.username,self.password)
        smtp.sendmail(self.sender,self.receivers,msg.as_string())  #发送
        smtp.quit()#关闭
if __name__=='__main__':
    Send_email(
        '15651797525@163.com',
        '15651797525@163.com',
        'xgh321324',
        [
            '15651797525@139.com',
            '970185127@qq.com'
        ],
        r'C:\Users\Administrator\Documents\GitHub\Medohealth\report\33.html').send()
    print(' 邮件发送成功！')