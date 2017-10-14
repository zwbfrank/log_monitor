import os
import sys
import django
import pymysql

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

if __name__ == '__main__':

	data = get_log_path()
	print(data)



