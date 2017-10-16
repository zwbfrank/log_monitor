#!/usr/bin/env python
import re
import send_mail as sm
from database_conn import get_log_path

# 匹配模式

pattern_error = r'.*\[ERROR\].*'
pattern_warning = r'.*(<info>).*'
pattern_error = re.compile(pattern_error)
pattern_warning = re.compile(pattern_warning)


# 获取服务器日志路径
log_path = get_log_path()

# 读取日志文件存入list或dict以便分析
# def get_log_lists(log_path):

# 	try:
# 		with open(log_path,'r',errors='ignore') as f_obj:
# 			log_lists = f_obj.readlines()
# 	except FileNotFoundError:
# 		pass
# 	else:
# 		return log_lists


# 分析日志
# def analysis_log(log_lists): 

# 	for log_list in log_lists:
# 		if log_list:
# 			# 日志错误信息匹配模式
# 			if re.match(pattern_error,log_list):
# 				pass
# 			# 警告信息匹配模式
# 			elif re.match(pattern_warning,log_list):
# 				# sm.send_email(log_list)
# 				print("hello")
		# else:
		# 	return
		# 	pass
		
class LogAnalyze():
	"""
		Log analyze.
	"""

	def __init__(self,log_path):
		self.log_path = log_path

	def get_log_lists(self):
		try:
			with open(self.log_path,'r',errors='ignore') as f_obj:
				log_lists = f_obj.readlines()
		except FileNotFoundError:
			pass
		else:
			return log_lists

	def log_analyze(self):
		log_lists = self.get_log_lists()
		for log_list in log_lists:
			if log_list:
				# 日志错误信息匹配模式
				if re.match(pattern_error,log_list):
					pass
				# 警告信息匹配模式
				elif re.match(pattern_warning,log_list):
					# sm.send_email(log_list)
					self.level = 'WARNING'
					return log_list







if __name__ == '__main__':

	# sm.send_email('hello')


	la = LogAnalyze(log_path)
	log_list = la.log_analyze()
	level = la.level
	print(level)
	print(log_list)