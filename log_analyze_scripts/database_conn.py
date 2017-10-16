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
	

def get_log_path():
	conn = pymysql_conn()
	cursor = conn.cursor()
	sql = 'select *from log_analyze_logmonitor'
	cursor.execute(sql)
	data = cursor.fetchall()
	log_path = data[0][2]
	cursor.close()
	conn.close()
	# conn.close()
	return log_path

# class DataConn():
# 	"""
# 		database connection about pymysql.
# 	"""

# 	def __init__(self,):
# 		pass

if __name__ == '__main__':


	log_path = get_log_path()
	la = lan.LogAnalyze(log_path)
	
	content = la.log_analyze()
	log_level = la.level
	conn = pymysql_conn()
	cursor = conn.cursor()

	cursor.execute("insert into log_analyze_logdata (id,log_type,log_level,content) values (%s,%s,%s,%s)",
					['2','PAYLOG',log_level,content])
	conn.commit()
	cursor.close()
	conn.close()




