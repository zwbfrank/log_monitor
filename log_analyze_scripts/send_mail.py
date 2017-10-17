#!/usr/bin/env python
import smtplib

from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr


#邮件地址
def _fromat_addr(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))


def send_email(message):

	from_addr = '18340865495@163.com'   #发件人邮箱地址
	password = 'zwbzwy125126'     #口令
	to_addr = '874032981@qq.com'   #收件人地址
	smtp_server = 'smtp.163.com'     #smtp协议地址

	msg = MIMEText(message,'plain','UTF-8')   #邮件文本对象
	msg['Subject'] = Header('Email test','utf-8').encode()
	msg['From'] = _fromat_addr('Pythoner<%s>'%from_addr)
	msg['To'] = _fromat_addr('管理员<%s>'%to_addr)

	try:
		server = smtplib.SMTP(smtp_server,25)   #连接smtp服务器
		server.login(from_addr,password)	#登录
		server.sendmail(from_addr,[to_addr],msg.as_string())
		server.quit()
	except :
		pass


if __name__ == '__main__':

	send_email('hello')
