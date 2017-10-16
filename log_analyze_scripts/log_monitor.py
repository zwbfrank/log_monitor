#!/usr/bin/env python
# coding:utf-8
import os
import signal
import subprocess
import time
from database_conn import get_log_path
#测试使用日志文件   
# logFile1="..\sample\sample_logs\log_json\_19_19_56.testlog"
logFile1 = get_log_path()
# with open(logFile1) as f:
# 	f = f.readline()
# 	print(f)
logFile2 = ""
#日志文件一般是按天产生，则通过在程序中判断文件的产生日期与当前时间，更换监控的日志文件  

def log_monitor(logFile):
	print("监控的日志文件是 %s"%logFile)
	# 程序运行10秒，监控另一个日志
	stoptime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+10))
	# 程序监控使用是linux命令tail -f来动态监控新追加的日志
	popen=subprocess.Popen('tail -f'+logFile,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
	pid=popen.pid
	print('Popen.pid:'+str(pid))
	while True:
		line=popen.stdout.readline().strip()
	# 判断内容是否为空
		if line:
			print(line)
			# 当前时间
			current_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			if current_time>=stoptime:
				# 终止子进程
				popen.kill()
				print('杀死subprocess')
				break
				time.sleep(2)
				log_monitor(logFile2)



if __name__=='__main__':

	log_monitor(logFile1)