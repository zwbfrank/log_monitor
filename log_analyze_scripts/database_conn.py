#!/usr/bin/env python

import pymysql
import log_analyze as lan

#databases config
config = {
	'db': 'log_DB',
	'user': 'root',
	'password': 'password',
	'host': '127.0.0.1',
	'port': 3306,
	'charset': 'utf8',
}

def pymysql_conn():
	conn = pymysql.connect(**config)
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
# class DataConn():
# 	"""
# 		database connection about pymysql.
# 	"""

# 	def __init__(self,):
# 		pass

if __name__ == '__main__':


	data = get_log_path_data()
	print(data)
	log_path = data[0][2]
	log_type = data[0][1]	
	# get_log_type()
	# log_type = get_log_type()
	# print(log_type)
	la = lan.LogAnalyze(log_path)
	la.log_analyze()
	# print(la.warning_log_lists)
	for log_list in la.warning_log_lists:
		# print('ok')

		# la.warning_log_lists
	
		content = log_list
		log_level = la.level
		conn = pymysql_conn()
		cursor = conn.cursor()

		cursor.execute("insert into log_analyze_logdata (log_type,log_level,content) values (%s,%s,%s)",
						[log_type,log_level,content])
		conn.commit()
		cursor.close()
		conn.close()




