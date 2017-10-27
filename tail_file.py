# 定时扫描目标目录，判断最新文件
# 扫描目标目录获取所有文件清单
# 通过比较文件最后时间获取新增文件
# 将最新文件更新到数据库
import os
import re
import time
import subprocess
from threading import Timer,Thread
from multiprocessing import Process,Queue
from datetime import date,time,datetime,timedelta
# import math


# print(os.listdir(os.path.expanduser("~")))



def search_newfile(dirname):
    """
    """
    directory = os.path.expanduser(dirname)
    print(directory)

    file_atime = {}

    list_file = os.listdir(directory)
    print(list_file)
    for f in list_file:
        if os.path.isfile(os.path.join(directory,f)):
            statinfo = os.stat(os.path.join(directory,f))
            file_atime[f] = statinfo.st_atime
            # print("file name: ",f)
            # print("file atime: ",statinfo.st_atime)
        # if os.path.isdir(os.path.join(directory,f)):
            # print("Directory: ",f)
    # print(file_atime)

    last_file = max(file_atime,key=file_atime.get)
    print(last_file)
    return last_file


# search_newfile('/var/log')

def timing_task(func,day=0,hour=0,min=0,second=0):
    now_time = datetime.now()
    format_now_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
    print("now: ",format_now_time)

    #task's timing
    timing = timedelta(days=day,hours=hour,minutes=min,seconds=second)
    next_time = now_time + timing
    format_next_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
    print("next run time: ",format_next_time)

    while True:
        #get current time
        now_time = datetime.now()
        format_now_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
        if str(format_now_time) == str(format_next_time):            
            print("start work: ",format_now_time)
            func()
            print("task done."+"\n\n")

            next_run_time = now_time + timing
            format_next_time = next_run_time.strftime('%Y-%m-%d %H:%M:%S')
            continue







def work():
    print("hello world.")




if __name__ == '__main__':


    # search_newfile('/var/log')
    dirname = '/var/log'
    # timing_task(search_newfile,dirname,second=45)
    timing_task(work,second=5)
