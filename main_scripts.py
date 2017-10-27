#!/usr/bin/env python
# coding:utf-8
import os
import re
import signal
import subprocess
import time
import smtplib

from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
import pymysql
import sys


# 匹配模式
pattern_error   = r'.*\[ERROR\].*'
pattern_warning = r'.*WARNING.*'
pattern_info    = r'.*<info>'
pattern_system  = r'.*\[system\].*'
pattern_error   = re.compile(pattern_error)
pattern_warning = re.compile(pattern_warning)
pattern_info    = re.compile(pattern_info)
pattern_system  = re.compile(pattern_system)


def pymysql_conn():
    # databases config
    config = {
        'db': 'log_DB',
        'user': 'root',
        'password': 'password',
        'host': '127.0.0.1',
        'port': 3306,
        'charset': 'utf8',
    }
    try:
        conn = pymysql.connect(**config)
    except:
        print("Cannot connect into database.")
    
    # cursor = conn.cursor()
    return conn

def get_log_path_data():
    conn = pymysql_conn()
    cursor = conn.cursor()
    sql = 'select *from log_analyze_logmonitor'
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data



# 获取服务器日志路径
# data = get_log_path_data()

# 读取日志文件存入list或dict以便分析
# def get_log_lists(log_path):

#   try:
#       with open(log_path,'r',errors='ignore') as f_obj:
#           log_lists = f_obj.readlines()
#   except FileNotFoundError:
#       pass
#   else:
#       return log_lists


# 分析日志
# def analysis_log(log_lists): 

#   for log_list in log_lists:
#       if log_list:
#           # 日志错误信息匹配模式
#           if re.match(pattern_error,log_list):
#               pass
#           # 警告信息匹配模式
#           elif re.match(pattern_warning,log_list):
#               # sm.send_email(log_list)
#               print("hello")
        # else:
        #   return
        #   pass
        
class LogAnalyze():

    """
        Log analyze.
    """

    def __init__(self,log_path):
        self.log_path = log_path
        self.error_log_lists   = []
        self.warning_log_lists = []
        self.info_log_lists    = []
        self.system_log_lists  = []
        self.level = ''

    def get_log_lists(self):
        try:
            with open(self.log_path,'r',errors='ignore') as f_obj:
                log_lists = f_obj.readlines()
        except FileNotFoundError:
            pass
        else:
            return log_lists

    def log_analyze(self):
        log_lists = self.get_log_lists()
        for log_list in log_lists:
            if log_list:
                # 日志错误信息匹配模式
                if re.match(pattern_error,log_list):
                    self.error_log_lists.append(log_list)
                    # self.level = 'ERROR'
                # 警告信息匹配模式
                elif re.match(pattern_warning,log_list):
                    # send_email(log_list)
                    self.warning_log_lists.append(log_list)
                    # self.level = 'WARNING'
                # info pattern
                elif re.match(pattern_info,log_list):
                    self.info_log_lists.append(log_list)
                    # self.level = 'INFO'
                # system pattern
                elif re.match(pattern_system,log_list):
                    self.system_log_lists.append(log_list)
                    # self.level = 'SYSTEM'
            


log_file = '/var/log/syslog'
#日志文件一般是按天产生，则通过在程序中判断文件的产生日期与当前时间，更换监控的日志文件  

stoptime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+10))
print(stoptime)

def log_monitor(log_file):
    print("监控的日志文件是 %s"%log_file)
    # 程序运行10秒，监控另一个日志

    # 程序监控使用是linux命令tail -f来动态监控新追加的日志
    popen=subprocess.Popen('tail -F '+log_file,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    pid=popen.pid
    print('Popen.pid:'+str(pid))
    while True:
        line=popen.stdout.readline().strip()
        # current_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        # print(current_time)
    # 判断内容是否为空
        if line:
            line = line.decode()
            print(line)
            # 当前时间
            current_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            print(current_time)
            if current_time >= stoptime:
                # 终止子进程
                popen.terminate()
                if subprocess.Popen.poll(popen) is not None:
                    break
                else:
                    print("wait for child process")
    print("done")
                # time.sleep(2)
                # log_monitor(logFile2)

if __name__ == '__main__':

    testlog = '/root/test2'
    # with open(testlog) as f:
    #     loglists = f.readlines()
    #     mark = f.tell()


    # log_monitor(log_file)
    # starttime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+10))
    # print(starttime)
    # popen = subprocess.Popen('tail -f '+log_file,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=True)
    # pid=popen.pid
    # print(str(pid))
    # print(starttime)
    # outputs = popen.stdout.readlines()
    # for output in outputs:
    #     print(output.decode())
    # time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    # print(time)



# #邮件地址
# def _fromat_addr(s):
#     name,addr = parseaddr(s)
#     return formataddr((Header(name,'utf-8').encode(),addr))
#
#
# def send_email(message):
#
#     from_addr = '18340865495@163.com'   #发件人邮箱地址
#     password = 'zwbzwy125126'           #口令
#     to_addr = '874032981@qq.com'        #收件人地址
#     smtp_server = 'smtp.163.com'        #smtp协议地址
#
#     msg = MIMEText(message,'plain','UTF-8')   #邮件文本对象
#     msg['Subject'] = Header('Email test','utf-8').encode()
#     msg['From'] = _fromat_addr('Pythoner<%s>'%from_addr)
#     msg['To'] = _fromat_addr('管理员<%s>'%to_addr)
#
#     try:
#         server = smtplib.SMTP(smtp_server,25)   #连接smtp服务器
#         server.login(from_addr,password)    #登录
#         server.sendmail(from_addr,[to_addr],msg.as_string())
#         server.quit()
#     except :
#         pass
#
#
# if __name__ == '__main__':
#
#
#
#
#     data = get_log_path_data()
#     print(data)
#     log_path = data[0][2]
#     log_type = data[0][1]
#
#     la = LogAnalyze(log_path)
#     la.log_analyze()
#     # print(la.warning_log_lists)
#     for log_list in la.error_log_lists:
#         content = log_list
#         if re.match(pattern_error,content):
#             log_level = 'ERROR'
#         conn = pymysql_conn()
#         cursor = conn.cursor()
#
#         cursor.execute("insert into log_analyze_userlogerror (log_type,log_level,content) values (%s,%s,%s)",
#                         [log_type,log_level,content])
#         conn.commit()
#         cursor.close()
#         conn.close()
#
#     for log_list in la.warning_log_lists:
#         content = log_list
#         if re.match(pattern_warning,content):
#             log_level = 'WARNING'
#         conn = pymysql_conn()
#         cursor = conn.cursor()
#
#         cursor.execute("insert into log_analyze_userlogwarning (log_type,log_level,content) values (%s,%s,%s)",
#                         [log_type,log_level,content])
#         conn.commit()
#         cursor.close()
#         conn.close()



    # def decode(s):
    #   return ''.join([chr(i) for i in [int(b,2) for b in s.split(' ')]])

    # log_monitor(logFile)
    
    # popen=subprocess.Popen('tail -f '+logfile,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    # lines = popen.stdout.readlines()
    # for line in lines:
    #   line = type(line)
    #   print(line)
    # for line in lines:
    #   print(line)
    # logfile='access.log'
    # starttime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    # command='tail -f '+logFile
    # popen=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    # # while True:
    # # lines=popen.stdout.readlines()
    # current_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    # print(stoptime)
    # print(current_time)
    # if current_time>=stoptime:
    #   popen.kill()
    # for line in lines:
    #   line = line.decode()
    # for line in lines:
    # lines = lines.decode()
    # print(lines)
    # popen.kill()

    # for line in line:
    #   line = type(line)
    #   print(line)
    # s = decode(line)
    # print(s)
    # print(line)
    # t = type(line)
    # print(t)
    # def encode(s):
 #      return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

    # def decode(s):
 #      return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


    # sm.send_email('hello')


    # la = LogAnalyze(log_path)
    # log_list = la.log_analyze()
    # level = la.level
    # print(level)
    # print(log_list)
    # print('ok')


    # log_path = '/var/log/testlog'
    # la = LogAnalyze(log_path)
    # la.log_analyze()
    # warn_list = la.error_log_lists
    # print(warn_list)
    # print(log_lists)