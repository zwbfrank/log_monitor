#!/usr/bin/env python
# coding:utf-8
import os
import re
import signal
import subprocess
from subprocess import Popen,PIPE
from time import sleep
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

def ssh_connect(hostname, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, port, username, password)
        return ssh
    except:
        pass

def get_94_info_file():
    # newest_file = []
    #ssh = ssh_connect('120.27.220.53', 8222, 'hsplan', 'wUrSLSoE%Jaih*sx%M')
    ssh = ssh_connect('116.62.57.219',8222,'hsplan','Li&2FMBQvsaO3mi6Ez')
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

def get_94_error_file():
    # newest_file = []
    #ssh = ssh_connect('120.27.220.53', 8222, 'hsplan', 'wUrSLSoE%Jaih*sx%M')
    ssh = ssh_connect('116.62.57.219',8222,'hsplan','Li&2FMBQvsaO3mi6Ez')
    # log_file = "biz-service-info.log"
    # command_cat = "cat /var/log/ppss_biz_service/" + log_file + "|grep ERROR"
    command_ls = "ls -rt /var/log/ppss_biz_service|tail -2"
    stdin, stdout, stderr = ssh.exec_command(command_ls)
    output = stdout.readlines()
    for i in range(len(output)):
        newest_file = output[i].strip()
        if pattern_error_file.match(newest_file):
            print(newest_file)
            ssh.close()
            return newest_file

def tail_94_info_file():
    conn = pymysql_conn()
    cursor = conn.cursor()
    create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    table = 'log_analyze_remotebizinfo94'
    insert = "INSERT INTO "+table+" (content,create_time) VALUES (%s,%s)"
    directory = "/var/log/ppss_biz_service/"
    #ssh = ssh_connect('120.27.220.53', 8222, 'hsplan', 'wUrSLSoE%Jaih*sx%M')
    ssh = ssh_connect('116.62.57.219',8222,'hsplan','Li&2FMBQvsaO3mi6Ez')
    biz_info = get_94_info_file()
    command_tail = "tail -F " + directory + biz_info
    stdin, stdout, stderr = ssh.exec_command(command_tail)
    try:
        while True:
            #sleep(1)
            output = stdout.readline().strip()
            if not output:
                continue
            print('ssh94 info: ',output)
            cursor.execute(insert,[output,create_time])
            conn.commit()
    except Exception as e:
        cursor.close()
        conn.close()

def tail_94_error_file():
    conn = pymysql_conn()
    cursor = conn.cursor()
    table = 'log_analyze_remotebizerror94'
    create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    insert = "INSERT INTO "+table+" (content,create_time) VALUES (%s,%s)"
    directory = "/var/log/ppss_biz_service/"
    #ssh = ssh_connect('120.27.220.53', 8222, 'hsplan', 'wUrSLSoE%Jaih*sx%M')
    ssh = ssh_connect('116.62.57.219',8222,'hsplan','Li&2FMBQvsaO3mi6Ez')
    biz_error = get_94_error_file()
    command_tail = "tail -F " + directory + biz_error
    stdin, stdout, stderr = ssh.exec_command(command_tail)
    try:
        while True:
            #sleep(1)
            output = stdout.readline().strip()
            if not output:
                continue
            print('ssh94 error: ',output)
            cursor.execute(insert,[output,create_time])
            conn.commit()
    except Exception as e:
        cursor.close()
        conn.close()
        
def get_98_info_file():
    # newest_file = []
    ssh = ssh_connect('120.27.222.33', 8222, 'hsplan', 'd3h%lM670%AVCuV5qG')
    #ssh = ssh_connect('116.62.57.219',8222,'hsplan','Li&2FMBQvsaO3mi6Ez')
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

def get_98_error_file():
    # newest_file = []
    ssh = ssh_connect('120.27.222.33', 8222, 'hsplan', 'd3h%lM670%AVCuV5qG')
    #ssh = ssh_connect('116.62.57.219',8222,'hsplan','Li&2FMBQvsaO3mi6Ez')
    # log_file = "biz-service-info.log"
    # command_cat = "cat /var/log/ppss_biz_service/" + log_file + "|grep ERROR"
    command_ls = "ls -rt /var/log/ppss_biz_service|tail -2"
    stdin, stdout, stderr = ssh.exec_command(command_ls)
    output = stdout.readlines()
    for i in range(len(output)):
        newest_file = output[i].strip()
        if pattern_error_file.match(newest_file):
            print(newest_file)
            ssh.close()
            return newest_file
        
def tail_98_info_file():
    conn = pymysql_conn()
    cursor = conn.cursor()
    create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    table = 'log_analyze_remotebizinfo98'
    insert = "INSERT INTO "+table+" (content,create_time) VALUES (%s,%s)"
    directory = "/var/log/ppss_biz_service/"
    ssh = ssh_connect('120.27.222.33', 8222, 'hsplan', 'd3h%lM670%AVCuV5qG')
    #ssh = ssh_connect('116.62.57.219',8222,'hsplan','Li&2FMBQvsaO3mi6Ez')
    biz_info = get_98_info_file()
    command_tail = "tail -F " + directory + biz_info
    stdin, stdout, stderr = ssh.exec_command(command_tail)
    try:
        while True:
            #sleep(1)
            output = stdout.readline().strip()
            if not output:
                continue
            print('ssh98 info: ',output)
            cursor.execute(insert,[output,create_time])
            conn.commit()
    except Exception as e:
        cursor.close()
        conn.close()

def tail_98_error_file():
    conn = pymysql_conn()
    cursor = conn.cursor()
    table = 'log_analyze_remotebizerror98'
    create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    insert = "INSERT INTO "+table+" (content,create_time) VALUES (%s,%s)"
    directory = "/var/log/ppss_biz_service/"
    ssh = ssh_connect('120.27.222.33', 8222, 'hsplan', 'd3h%lM670%AVCuV5qG')
    #ssh = ssh_connect('116.62.57.219',8222,'hsplan','Li&2FMBQvsaO3mi6Ez')
    biz_error = get_98_error_file()
    command_tail = "tail -F " + directory + biz_error
    stdin, stdout, stderr = ssh.exec_command(command_tail)
    try:
        while True:
            #sleep(1)
            output = stdout.readline().strip()
            if not output:
                continue
            print('ssh98 error: ',output)
            cursor.execute(insert,[output,create_time])
            conn.commit()
    except Exception as e:
        cursor.close()
        conn.close()

def main():
    tasks = (tail_94_info_file,tail_94_error_file,tail_98_info_file,tail_98_error_file)
    pool = Pool(4)
    for task in tasks:
        pool.apply_async(task)
    pool.close()
    pool.join()
        
if __name__ == '__main__':
    main()



        