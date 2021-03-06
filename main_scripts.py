#!/usr/bin/env python
# coding:utf-8
import os
import re
import signal
import subprocess
import time
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
import pymysql
import paramiko

import sys

from threading import Timer,Thread
from multiprocessing import Process, Queue,Pool
from datetime import time, datetime, timedelta
# from global_variable import local_newest_files,ssh_newest_file,log_type,log_path

DEFAULT_LOG_PATH = ['/var/log/ppss_biz_service','/var/log/ppss_order_service/','/var/log/ppss_pay_service/',
                    '/var/log/ppss_shop_service/','/var/log/ppss_wx_service/','/var/log/ppss_user_service/',
                    '/var/log/ppss_alibblife_web/','/var/log/ppss_alilife_service','/var/log/ppss_admin_web',
                    '/var/log/ppss_communication_service','/var/log/ppss_mobile_web','/var/log/ppss_config_service',
                    '/var/log/ppss_promotion_service','/var/log/ppss_wap_web']

dirname_dict = {
    'biz': '/var/log/ppss_biz_service',
    'alibblife': '/var/log/ppss_alibblife_web',
    'admin': '/var/log/ppss_admin_web',
    'alilife': '/var/log/ppss_alilife_service',
    'commun': '/var/log/ppss_communication_service',
    'config': '/var/log/ppss_config_service',
    'mobile': '/var/log/ppss_mobile_web',
    'order': '/var/log/ppss_order_service',
    'pay': '/var/log/ppss_pay_service',
    'promotion': '/var/log/ppss_promotion_service',
    'shop': '/var/log/ppss_shop_service',
    'wap': '/var/log/ppss_wap_web',
    'wx': '/var/log/ppss_wx_service',
    'user': '/var/log/ppss_user_service',
}

table_dict = {
    'biz': 'log_analyze_bizserviceerror',
    'alibblife': 'log_analyze_alibblifeweberror',
    'admin': 'log_analyze_adminweberror',
    'alilife': 'log_analyze_alilifeserviceerror',
    'commun': 'log_analyze_communicationserviceerror',
    'config': 'log_analyze_configserviceerror',
    'mobile': 'log_analyze_mobileweberror',
    'order': 'log_analyze_orderserviceerror',
    'pay': 'log_analyze_payserviceerror',
    'promotion': 'log_analyze_promotionserviceerror',
    'shop': 'log_analyze_shopserviceerror',
    'wap': 'log_analyze_wapweberror',
    'wx': 'log_analyze_wxserviceerror',
    'user': 'log_analyze_userserviceerror',
}

# 匹配模式
pattern_error         = r'.*\[ERROR\].*'
pattern_warning       = r'.*WARNING.*'
pattern_info_file     = r'.*(info\.log)$'
pattern_error_file    = r'.*(error\.log)$'
pattern_system        = r'.*\[system\].*'
pattern_admin         = r'^Nov\s+(14).*'
pattern_admin         = re.compile(pattern_admin)
pattern_error         = re.compile(pattern_error)
pattern_warning       = re.compile(pattern_warning)
pattern_info_file     = re.compile(pattern_info_file)
pattern_system        = re.compile(pattern_system)
pattern_error_file    = re.compile(pattern_error_file)

def pymysql_conn():
    # databases config
    config = {
        'db': 'log_monitor',
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
            

#邮件地址
def fromat_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

def send_email(message):

    from_addr = '18340865495@163.com'   #发件人邮箱地址
    password = 'zwbzwy125126'           #口令
    to_addr = '874032981@qq.com'        #收件人地址
    smtp_server = 'smtp.163.com'        #smtp协议地址

    msg = MIMEText(message,'plain','UTF-8')   #邮件文本对象
    msg['Subject'] = Header('Email test','utf-8').encode()
    msg['From'] = fromat_addr('Pythoner<%s>'%from_addr)
    msg['To'] = fromat_addr('管理员<%s>'%to_addr)

    try:
        server = smtplib.SMTP(smtp_server,25)   #连接smtp服务器
        server.login(from_addr,password)    #登录
        server.sendmail(from_addr,[to_addr],msg.as_string())
        server.quit()
    except :
        pass

def ssh_connect(hostname, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, port, username, password)
        return ssh
    except:
        pass

def get_ssh_newest_file():
    # newest_file = []
    ssh = ssh_connect('120.27.220.53', 8222, 'hsplan', 'wUrSLSoE%Jaih*sx%M')
    # log_file = "biz-service-info.log"
    # command_cat = "cat /var/log/ppss_biz_service/" + log_file + "|grep ERROR"
    command_ls = "ls -rt /var/log/ppss_biz_service|tail -2"
    stdin, stdout, stderr = ssh.exec_command(command_ls)
    output = stdout.readlines()
    for i in range(len(output)):
        newest_file = output[i].strip()
        if pattern_info_file.match(newest_file):
            print(newest_file)
            ssh.close()
            return newest_file
        # newest_file.append(line)
        # if line not in ssh_newest_file:
        #     ssh_newest_file.append(line)
            # print(line)
    # print(ssh_newest_file)
    # return newest_file

def cat_ssh_newest_file(directory):
    # directory = "/var/log/ppss_biz_service/"
    conn = pymysql_conn()
    cursor = conn.cursor()
    ssh = ssh_connect('120.27.220.53', 8222, 'hsplan', 'wUrSLSoE%Jaih*sx%M')
    ssh_newest_file = get_ssh_newest_file()
    log_file = ssh_newest_file

    command_cat = "cat " + directory + log_file + "|grep ERROR"
    sdin, stdout, stderr = ssh.exec_command(command_cat)
    log_type = 'BIZ'
    log_level = 'ERROR'
    lines = stdout.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        cursor.execute("INSERT INTO log_analyze_bizserviceerror (log_type,log_level,content) VALUES (%s,%s,%s)",
                        [log_type,log_level,line])
        conn.commit()
    cursor.close()
    conn.close()
    ssh.close()

def read_ssh_newest_file():
    directory = "/var/log/ppss_biz_service/"
    conn = pymysql_conn()
    cursor = conn.cursor()
    ssh = ssh_connect('120.27.220.53', 8222, 'hsplan', 'wUrSLSoE%Jaih*sx%M')
    try:
        ssh_newest_file = get_ssh_newest_file()
        command_cat = "cat " + directory + ssh_newest_file + "|grep ERROR"
        sdin, stdout, stderr = ssh.exec_command(command_cat)
        log_type = 'BIZ'
        log_level = 'ERROR'
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        lines = stdout.readlines()
        for i in range(len(lines)):
            line = lines[i].strip()
            if line:
                print(line)
                cursor.execute("INSERT INTO log_analyze_bizserviceerror (log_type,log_level,content,create_time) VALUES (%s,%s,%s,%s)",
                                [log_type,log_level,line,create_time])
                conn.commit()
        command_tail = "tail -F " + directory + ssh_newest_file+"|grep ERROR"
        stdin, stdout, stderr = ssh.exec_command(command_tail)
        while True:
            line = stdout.readline().strip()
            if not line:
                continue
            print(line)
    except:
        cursor.close()
        conn.close()
        ssh.close()

def tail_ssh_newest_file():
    directory = "/var/log/ppss_biz_service/"
    ssh = ssh_connect('120.27.220.53', 8222, 'hsplan', 'wUrSLSoE%Jaih*sx%M')
    ssh_newest_file = get_ssh_newest_file()
    log_file = ssh_newest_file
    command_tail = "tail -F " + directory + log_file
    stdin, stdout, stderr = ssh.exec_command(command_tail)
    while True:
        output = stdout.readline().strip()
        if not output:
            continue
        print(output)

def search_new_file(dirname):
    """
    """
    # dirname = '/var/log'
    directory = os.path.expanduser(dirname)
    # print(directory)

    file_mtime = {}

    list_file = os.listdir(directory)
    # print(list_file)
    if list_file is not None:
        for f in list_file:
            if os.path.isfile(os.path.join(directory, f)):
                stat_info = os.stat(os.path.join(directory, f))
                file_mtime[f] = stat_info.st_mtime

    newest_file = max(file_mtime, key=file_mtime.get)

    # if newest_file not in local_newest_files:
    #     local_newest_files.append(newest_file)
    #     # new_file_path = os.path.join(directory,newest_file)
    #     print("newest file is: ",newest_file)
    return newest_file



def read_log_new_file(key):
    dirname = dirname_dict[key]
    conn = pymysql_conn()
    cursor = conn.cursor()
    log_type = 'HSPLAN'
    log_level = 'ERROR'
    create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    table = table_dict[key]
    insert = "INSERT INTO "+table+" (log_type,log_level,content,create_time) VALUES (%s,%s,%s,%s)"
    newest_file = search_new_file(dirname)
    print("正在监控的文件： ",newest_file)
    newest_file_path = os.path.join(dirname,newest_file)
    offset_path = os.path.dirname(os.path.abspath(__file__))
    # file_size = os.path.getsize(last_file_path)
    with open(newest_file_path) as f:
        if pattern_info_file.match(newest_file):            
            try:
                with open(offset_path+'/offset/'+key+'_info_offset.txt') as f_off:
                    # 获取当前文件自上次读取后的偏移量
                    offset = f_off.read().strip()
                    print("读取后的offset: ",offset)
                    file_size = os.path.getsize(newest_file_path)
                    if file_size < int(offset):
                        offset = 0
                        print("新文件的offset: ",offset)
            except FileNotFoundError:
                offset = 0
                print("offset文件不存在: ",offset)
                
            f.seek(int(offset),0)
            while True:
                line = f.readline().rstrip()
                if not line:
                    break
                elif re.match(pattern_error,line):
                    print(line)
                    cursor.execute(insert,[log_type,log_level,line,create_time])
                    conn.commit()
            offset = f.tell()
            
            with open(offset_path+'/offset/'+key+'_info_offset.txt','w') as f_off:
                # 将操作文件后的偏移量以覆盖方式存入文件
                f_off.write(str(offset))
        if pattern_error_file.match(newest_file):
            try:
                with open(offset_path+'/offset/'+key+'_error_offset.txt') as f_off:
                    # 获取当前文件自上次读取后的偏移量
                    offset = f_off.read().strip()
                    print("读取后的offset: ",offset)
                    file_size = os.path.getsize(newest_file_path)
                    if file_size < int(offset):
                        offset = 0
                        print("新文件的offset: ",offset)
            except FileNotFoundError:
                offset = 0
                print("offset文件不存在: ",offset)
                
            f.seek(int(offset),0)
            while True:
                line = f.readline().rstrip()
                if not line:
                    break
                elif re.match(pattern_error,line):
                    print(line)
                    cursor.execute(insert,[log_type,log_level,line,create_time])
                    conn.commit()
            offset = f.tell()
            
            with open(offset_path+'/offset/'+key+'_error_offset.txt','w') as f_off:
                # 将操作文件后的偏移量以覆盖方式存入文件
                f_off.write(str(offset))

        cursor.close()
        conn.close()

def tail_file():
    dirname = '/var/log'
    last_file_path = os.path.join(dirname,search_new_file(dirname))
    conn = pymysql_conn()
    cursor = conn.cursor()
    log_type = 'SYSTEM'
    log_level = 'COMMON'
    insert = "INSERT INTO log_analyze_adminweberror (log_type,log_level,content) VALUES (%s,%s,%s)"
    with open(last_file_path) as f:
        with open('./offset.txt') as f_off:
            offset = f_off.read().strip()

        f.seek(int(offset),0)
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            cursor.execute(insert,[log_type,log_level,line])
            conn.commit()
        offset = f.tell()

        with open('./offset.txt','w') as f_off:
            f_off.write(str(offset))
    cursor.close()
    conn.close()
    
def timing_task(func, arg=None, args=None, kwargs=None, day=0, hour=0, minute=0, second=10):
    now_time = datetime.now()
    format_now_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
    print("now: ", format_now_time)

    # task's timing
    timing = timedelta(days=day, hours=hour, minutes=minute, seconds=second)
    next_time = now_time + timing
    format_next_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
    print("next run time: ", format_next_time)

    while True:
        # get current time
        now_time = datetime.now()
        format_now_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
        if str(format_now_time) == str(format_next_time):
            print("start work: ",format_now_time)
            start_time = datetime.now()
            if arg is not None:
                func(arg)
            elif args is not None:
                func(*args)
            elif kwargs is not None:
                func(**kwargs)
            else:
                func()
            end_time = datetime.now()
            task_time = end_time - start_time
            print("task done."+"\n\n")
    
            next_run_time = now_time + timing + task_time
            format_next_time = next_run_time.strftime('%Y-%m-%d %H:%M:%S')
            continue
            
def main():
    tasks = [read_user_new_file,
             read_wx_new_file,
             read_wap_new_file,
             read_shop_new_file,
             read_promotion_new_file,
             read_pay_new_file,
             read_order_new_file,
             read_mobile_new_file,
             read_config_new_file,
             read_commun_new_file,
             read_alilife_new_file,
             read_admin_new_file,
             read_biz_new_file]
    pool = Pool()
    for key in table_dict:
        pool.apply(read_log_new_file,(key,))
    pool.close()
    pool.join()
            
if __name__=='__main__':
    main()




        



    



