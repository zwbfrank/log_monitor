from django.db import models

TYPE_CHOICES = (
	('TP1','USERLOG'),
	('TP2','PAYLOG'),
)

# Create your models here.
class LogMonitor(models.Model):
	log_type = models.CharField(max_length=10,choices=TYPE_CHOICES)
	log_path = models.CharField(max_length=200)
	timing = models.IntegerField()

	def __str__(self):
		return self.log_type

class LogData(models.Model):
	log_type = models.CharField(max_length=10,choices=TYPE_CHOICES)
	log_level = models.CharField(max_length=10)
	content = models.TextField()

	def __str__(self):
		return self.log_type
		pass

