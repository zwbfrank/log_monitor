import pymysql
from database_config import config


class DBOperation():
	"""
		About database operation,such as select,insert,delete,update.
	"""

	def __init__(self,conn):
		self.conn = conn

	def get_cursor(self):
		conn = self.conn
		cursor = conn.cursor()
		return cursor

	def select(self,):
		cursor = self.get_cursor()
		sql = ""
		pass