#!/usr/bin/env python
# coding:utf-8
"""
模块名：test
功能：将测试服务器日志实时存入数据库
"""

import os
import re
import signal
import subprocess
from time import *
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
import pymysql
# import paramiko

import sys

from threading import Timer,Thread
from multiprocessing import Process, Queue,Pool
from datetime import datetime, timedelta


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

pattern_admin_web     = r'.*admin_web$'
ppss_admin_web        = re.compile(pattern_admin_web)
pattern_user_service  = r'.*user_service$'
ppss_user_service     = re.compile(pattern_user_service)
pattern_ppss          = r'(.*admin_web$)|(.*user_service$)'
pattern_ppss          = re.compile(pattern_ppss)

pattern_new_log       = re.compile(r'(.*error\.log)$|(.*info\.log)$')

def pymysql_conn():
    # databases config
    config = {
        'db': 'ppss_log',
        'user': 'log_user',
        'password': 'hsplan.2017',
        'host': 'rm-bp1mnhth64d8zx0q6.mysql.rds.aliyuncs.com',
        'port': 3306,
        'charset': 'utf8',
    }
    try:
        conn = pymysql.connect(**config)
    except:
        print("Cannot connect into database.")
    
    # cursor = conn.cursor()
    return conn

def search_new_file(dirname):
    dir_list_file = os.listdir(dirname)
    # print(dir_list_file)
    if dir_list_file is not None:
        new_file_list = [file for file in dir_list_file if pattern_new_log.match(file)]
    return new_file_list

def get_info_file(dirname):
    new_file_list = search_new_file(dirname)
    for file in new_file_list:
        if pattern_info_file.match(file):
            return file

def get_error_file(dirname):
    new_file_list = search_new_file(dirname)
    for file in new_file_list:
        if pattern_error_file.match(file):
            return file

def read_info_new_file(key):
    """
    功能：读取info日志内容到数据库
    :param key:
    :return:
    """
    conn = pymysql_conn()
    cursor = conn.cursor()
    log_type = 'HSPLAN'
    log_level = 'ERROR'
    create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    table = table_dict[key]
    insert = "INSERT INTO "+table+" (log_type,log_level,content,create_time) VALUES (%s,%s,%s,%s)"
    
    dirname = dirname_dict[key]
    new_info_file = get_info_file(dirname)
    print("new info file: ",new_info_file)
    info_file_path = os.path.join(dirname,new_info_file)
    info_file_size = os.path.getsize(info_file_path)
    offset_path = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(info_file_path) as f:
            try:
                with open(offset_path+'/offset/'+key+'_info_offset.txt') as f_offset:
                    # 获取当前文件自上次读取后的偏移量
                    offset = f_offset.read().strip()
                    print("读取后的offset: ",offset)
                    if info_file_size < int(offset):
                        offset = 0
                        print("文件更新,初始化offset: ",offset)
            except FileNotFoundError:
                offset = 0
                print("首次运行,初始化offset: ",offset)
            
            f.seek(int(offset),0)
            while True:
                line = f.readline().strip()
                if not line:
                    break
                elif re.match(pattern_error,line):
                    cursor.execute(insert,[log_type,log_level,line,create_time])
                    conn.commit()
            offset = f.tell()
            with open(offset_path+'/offset/'+key+'_info_offset.txt','w') as f_offset:
                f_offset.write(str(offset))
    except FileNotFoundError:
        pass
    cursor.close()
    conn.close()

def read_error_new_file(key):
    """
    功能：读取error日志文件内容存到数据库
    :param key:通过key可以获取字典中对应的日志目录和数据库表
    :return:
    """
    conn = pymysql_conn()
    cursor = conn.cursor()
    log_type = 'HSPLAN'
    log_level = 'ERROR'
    create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    table = table_dict[key]
    insert = "INSERT INTO " + table + " (log_type,log_level,content,create_time) VALUES (%s,%s,%s,%s)"
    
    dirname = dirname_dict[key]
    new_error_file = get_error_file(dirname)
    print("new error file: ", new_error_file)
    info_file_path = os.path.join(dirname, new_error_file)
    info_file_size = os.path.getsize(info_file_path)
    offset_path = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(info_file_path) as f:
            try:
                with open(offset_path + '/offset/' + key + '_error_offset.txt') as f_offset:
                    # 获取当前文件自上次读取后的偏移量
                    offset = f_offset.read().strip()
                    print("读取后的offset: ", offset)
                    if info_file_size < int(offset):
                        offset = 0
                        print("文件更新,初始化offset: ", offset)
            except FileNotFoundError:
                offset = 0
                print("首次运行,初始化offset: ", offset)
            
            f.seek(int(offset), 0)
            while True:
                line = f.readline().strip()
                if not line:
                    break
                elif re.match(pattern_error, line):
                    cursor.execute(insert, [log_type, log_level, line, create_time])
                    conn.commit()
            offset = f.tell()
            with open(offset_path + '/offset/' + key + '_error_offset.txt', 'w') as f_offset:
                f_offset.write(str(offset))
    except FileNotFoundError:
        pass
    cursor.close()
    conn.close()

def str2sec(t):
    """
    将字符格式时间转化成秒数
    :param t:
    :return: 以秒为单位的时间
    """
    h,m,s = str(t).split(':')
    return int(h)*3600+int(m)*60+int(s)

def timing_task(func, arg=None, args=None, kwargs=None, day=0, hour=0, minute=0, second=10):
    """
    功能：定时执行func任务
    :param func:指定的方法名
    :param arg:方法所需单个参数
    :param args: 列表参数
    :param kwargs:字典参数
    :param day:以天为单位循环执行任务
    :param hour:
    :param minute:
    :param second:
    :return: None
    """
    now_time = datetime.now()
    format_now_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
    print("now: ", format_now_time)

    # task's timing
    timing = timedelta(days=day, hours=hour, minutes=minute, seconds=second)
    #sleep_time = str2sec(timing)
    next_run_time = now_time + timing
    format_next_time = next_run_time.strftime('%Y-%m-%d %H:%M:%S')
    print("next run time: ", format_next_time)

    while True:
        # get current time
        now_time = datetime.now()
        format_now_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
        if str(format_now_time) >= str(format_next_time):
            print("start work:"+format_now_time)
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
        sleep(1)
        
def main():
    """
    多进程处理任务
    pool是进程池对象
    """
    pool = Pool()
    for key in table_dict:
        pool.apply(read_info_new_file,(key,))
        pool.apply(read_error_new_file,(key,))
    pool.close()
    pool.join()
            
if __name__=='__main__':
    main()







        
