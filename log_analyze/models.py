from django.db import models
import django

TYPE_CHOICES = (
	('USER','USERLOG'),
	('PAY','PAYLOG'),
)

# Create your models here.
class LogMonitor(models.Model):
	log_type = models.CharField(max_length=100,choices=TYPE_CHOICES)
	log_path = models.CharField(max_length=200)
	timing = models.IntegerField()

	def __str__(self):
		return self.log_type


class UserLogSystem(models.Model):
	# log_type = models.ForeignKey(LogMonitor,on_delete=models.CASCADE)
	log_type = models.CharField(max_length=225)
	log_level = models.CharField(max_length=225)
	content = models.TextField()

	def __str__(self):
		return self.content


class UserLogWarning(models.Model):
	log_type = models.CharField(max_length=225)
	log_level = models.CharField(max_length=225)
	content = models.TextField()

	def __str__(self):
		return self.content


class UserLogError(models.Model):
	log_type = models.CharField(max_length=225)
	log_level = models.CharField(max_length=225)
	content = models.TextField()

	def	__str__(self):
		return self.content


class UserLogInfo(models.Model):
	log_type = models.CharField(max_length=225)
	log_level = models.CharField(max_length=225)
	content = models.TextField()

	def __str__(self):
		return self.content


class LogLevel(models.Model):
	level = models.CharField(max_length=225)
	desc = models.CharField(max_length=225)

	def __str__(self):
		return self.level