import os
from time import ctime,sleep
import time
from threading import Timer,Thread
import subprocess
import paramiko
from multiprocessing import Queue,Process


log_file = '/var/log/syslog'
test_log = '/var/log/testlog'
def log_monitor(log_file):
    
    pid = os.getpid()
    print("Parent's pid: "+str(pid))
    print("监控的日志文件是 %s"%log_file)
    # 程序运行15秒，监控另一个日志
    # endtime = time.time()+15
    # print("end time: ",endtime)
    # 程序监控使用是linux命令tail -f来动态监控新追加的日志
    popen=subprocess.Popen('tail -f '+test_log,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    popen.wait()
    pid=popen.pid
    print('Popen.pid:'+str(pid))
    lines = popen.stdout.read()
    print(lines)
    # while True:
    #     # print("start")
    #     line = popen.stdout.readline().strip().decode()
    #     print(line)
    #     popen.wait()
        # if line:
        #     line = line.decode('utf-8')
        #     print(line)
        #     current_time = time.time()
        #     if current_time>=endtime:
        #         print("current_time: ",current_time)
        #         popen.terminate()
        #         break
        #     else:
        #         print("fail")






 # def test_monitor():


    # while True:
    #     line=popen.stdout.readline().strip()
    #     # current_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #     # print(current_time)
    # # 判断内容是否为空
    #     if line:
    #         line = line.decode()
    #         print(line)
    #         # 当前时间
    #         current_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #         print(current_time)
    #         if current_time >= stoptime:
    #             # 终止子进程
    #             popen.terminate()
    #             if subprocess.Popen.poll(popen) is not None:
    #                 break
    #             else:
    #                 print("wait for child process")


# def main():
# 	p = Process(log_monitor)



if __name__ == '__main__':
    log_monitor(log_file)
    # main()

	# with open(log_file) as f:
	# 	f.readline()


	# mylist = (x*x for x in range(3))

	# log_monitor(log_file)
    # with open(log_file) as f:
     #    endtime = time.time()
     #    while True:
     #        line = f.readline().strip()
     #        if line !='':
     #            print(line)
     #        else:
     #            break



    # endtime = time.localtime(time.time()+15)
	# print("end time: ",endtime)
	# while True:
	# 	clock = time.localtime(time.time())
	# 	print(clock)
	# 	sleep(1)
	# 	if clock>=endtime:
	# 		print(clock)
	# 		print("timeout")
	# 		break 