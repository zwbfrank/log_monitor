from subprocess import Popen,PIPE
import time
import multiprocessing
import os
from tail_file import timing_task

# def func(msg):
#     for i in range(4):
#         print(msg)
#         time.sleep(3)
#     print('\n')
#     return "done " + msg

if __name__ == "__main__":
	file = '/var/log/newfile0'
	# file_path = unicode(file,'utf8')
	fsize = os.path.getsize(file)
	print(fsize)
	with open(file) as f:
		line = f.read()
		offset = f.tell()
		print(offset)




# 	file = '/var/log/newfile0'
# 	stat_info = os.stat(file)
# 	file_ctime = stat_info.st_ctime
# 	file_mtime = stat_info.st_mtime
# 	file_atime = stat_info.st_atime
# 	print("first time: ")
# 	print('ctime: ',file_ctime)
# 	print('mtime: ',file_mtime)
# 	print('atime: ',file_atime)
# 	time.sleep(5)
# 	print('\n')
# 	print('second time: ')
# 	file_ctime = stat_info.st_ctime
# 	file_mtime = stat_info.st_mtime
# 	file_atime = stat_info.st_atime

# 	print('ctime: ',file_ctime)
# 	print('mtime: ',file_mtime)
# 	print('atime: ',file_atime)
# 	time.sleep(5)
# 	print('\n')
# 	print('third time: ')
# 	file_ctime = stat_info.st_ctime
# 	file_mtime = stat_info.st_mtime
# 	file_atime = stat_info.st_atime
# 	with open(file) as f:
# 		file = f.read().strip()
# 		print(file)
# 	print('ctime: ',file_ctime)
# 	print('mtime: ',file_mtime)
# 	print('atime: ',file_atime)	





#     func
#     pool = multiprocessing.Pool(processes=4)
#     result = []
#     for i in range(4):
#         msg = "hello %d" %(i)
#         result.append(pool.apply_async(func, (msg, )))
#     pool.close()
#     pool.join()
#     for res in result:
#         print(res.get())
#     print("Sub-process(es) done.")


# with open('/root/test1') as f1:

#     print(f1.tell())
#     print(f1.readline().rstrip())
#     print(f1.tell())
#     offset = f1.tell() 
#     # f1.seek(offset, 0)
#     # print(f1.tell())
#     # print(f1.readline())
# with open('/root/test1') as f2:
# 	f2.seek(offset,0)
# 	# print('f2:',f2.readline().rstrip())
# 	while True:
# 		line = f2.readline().rstrip()
# 		if not line:
# 			break
# 		print(line)
# 	offset = f2.tell()
# 	with open('/root/offset.txt','w') as f_off:
# 		f_off.write(str(offset))

def tail_file():
	with open('/root/test1') as f:
		with open('/root/offset.txt') as f_off:
			offset = f_off.read().strip()
			f.seek(int(offset),0)
			# print('f2:',f2.readline().rstrip())
			while True:
				line = f.readline().rstrip()
				if not line:
					break
				print(line)
			offset = f.tell()
		with open('/root/offset.txt','w') as f_off:
			f_off.write(str(offset))

# import re
# if __name__ == '__main__':
# 	# timing_task(tail_file,second=5)
# 	with open('/var/log/syslog') as f:
# 		while True:
# 			line = f.readline().rstrip()
# 			if not line:
# 				break
# 			elif re.match(r'^[Nov\s\d]+',line):
# 				print(line)
   

def search_last_mfile(dirname):
    """
    """
    # dirname = '/var/log'
    directory = os.path.expanduser(dirname)
    # print(directory)

    file_mtime = {}

    list_file = os.listdir(directory)
    # print(list_file)

    for f in list_file:
        if os.path.isfile(os.path.join(directory, f)):
            stat_info = os.stat(os.path.join(directory, f))
            file_mtime[f] = stat_info.st_mtime

    last_mfile = max(file_mtime, key=file_mtime.get)

    # if last_mfile not in local_newest_files:
    #     local_newest_files.append(last_mfile)
    #     # new_file_path = os.path.join(directory,last_mfile)
    #     print("newest file is: ",last_mfile)
    return last_mfile

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
        if os.path.isfile(os.path.join(directory, f)):
            stat_info = os.stat(os.path.join(directory, f))
            file_atime[f] = stat_info.st_atime

    last_afile = max(file_atime, key=file_atime.get)

    # if last_mfile not in local_newest_files:
    #     local_newest_files.append(last_mfile)
    #     # new_file_path = os.path.join(directory,last_mfile)
    #     print("newest file is: ",last_mfile)
    return last_afile


def read_new_file():
    # errors = []
    # global offset
    dirname = '/var/log/'
    conn = pymysql_conn()
    cursor = conn.cursor()
    log_type = 'SYSTEM'
    log_level = 'COMMON'
    insert = "INSERT INTO log_analyze_adminweberror (log_type,log_level,content) VALUES (%s,%s,%s)"
    last_mfile = search_last_mfile(dirname)
    # last_afile = search_new_file(dirname)
    # last_mfile_path = os.path.join(dirname,last_mfile)
    # last_afile_path = os.path.join(dirname,last_afile)
    if last_mfile == last_afile:
    	last_file_path = os.path.join(dirname,last_mfile)




    # with open(last_file_path) as f:
    #     with open('/root/offset.txt') as f_off:
    #         # 获取当前文件自上次读取后的偏移量
    #         offset = f_off.read().strip()

    #     f.seek(int(offset),0)
    #     while True:
    #         line = f.readline().rstrip()
    #         if not line:
    #             break
    #         elif re.match(r'^[Nov\s\d]+',line):
    #             print(line)
    #             cursor.execute(insert,[log_type,log_level,line])
    #             conn.commit()
    #     offset = f.tell()

    #     with open('/root/offset.txt','w') as f_off:
    #         # 将操作文件后的偏移量以覆盖方式存入文件
    #         f_off.write(str(offset))
    # cursor.close()
    # conn.close()


# if last_mfile is new_file:
# 	file_offset = null
# 	if file_offset is null:
# 		offset = 0
# 	else:
# 		offset = file_offset.read()
# 	last_mfile.seek(int(offset),0)
# else:
# 	if file_offset is null:
# 		offset = 0
# 	else:
# 		offset = file_offset.read()










# lines = []
# endtime = time.time()+120
# cmd = 'tail -1F /var/log/newfile1'
# p = Popen(cmd,stdout=PIPE,stderr=PIPE,stdin=PIPE,shell=True)
# pid = p.pid
# print(str(pid))
# while True:
#   line = p.stdout.readline().rstrip()
#   if line:
#         # line = line.decode()
#       lines.append(line)
#       print(line)
#   thistime = time.time()
#   if thistime>=endtime:
#       p.kill()
#       break
# p.wait()
# print(lines)



