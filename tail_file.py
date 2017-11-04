# 定时扫描目标目录，判断最新文件
# 扫描目标目录获取所有文件清单
# 通过比较文件最后时间获取新增文件
# 将最新文件更新到数据库
import os
import re
import time
import subprocess
# from threading import Timer,Thread
from multiprocessing import Process,Queue
from datetime import date,time,datetime,timedelta
# import math
from global_variable import local_newest_files

# print(os.listdir(os.path.expanduser("~")))



def search_new_file(dirname):
    """
    """
    # dirname = '/var/log'
    directory = os.path.expanduser(dirname)
    # print(directory)

    file_atime = {}
    
    list_file = os.listdir(directory)
    # print(list_file)

    for f in list_file:
        if os.path.isfile(os.path.join(directory,f)):
            stat_info = os.stat(os.path.join(directory,f))
            file_atime[f] = stat_info.st_atime
    
    last_file = max(file_atime,key=file_atime.get)
    
    if last_file not in local_newest_files:
        local_newest_files.append(last_file)
        new_file_path = os.path.join(directory,last_file)
        print(last_file)
        # return last_file
        return new_file_path
    
def log_analyze():
    new_file_path = search_new_file()
    


# search_newfile('/var/log')

def timing_task(func,arg=None,args=None,kwargs=None,day=0,hour=0,minute=0,second=0):
    now_time = datetime.now()
    format_now_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
    print("now: ",format_now_time)

    #task's timing
    timing = timedelta(days=day,hours=hour,minutes=minute,seconds=second)
    next_time = now_time + timing
    format_next_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
    print("next run time: ",format_next_time)

    while True:
        #get current time
        now_time = datetime.now()
        format_now_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
        if str(format_now_time) == str(format_next_time):
            # print("start work: ",format_now_time)
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
            task_time = end_time-start_time
            # print("task done."+"\n\n")

            next_run_time = now_time + timing + task_time
            format_next_time = next_run_time.strftime('%Y-%m-%d %H:%M:%S')
            continue

# def







def work():
    print("hello world.")




if __name__ == '__main__':

    # # search_new_file('/var/log')
    # dirname = '/var/log'
    # # timing_task(search_new_file,dirname,second=45)
    # timing_task(search_new_file,dirname,second=5)
    # # timing_task(work,second=5)
    # # print(local_newest_files)
    
    

