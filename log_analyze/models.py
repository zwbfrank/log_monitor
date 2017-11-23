from django.db import models
import django.utils.timezone as timezone

TYPE_CHOICES = (
    ('USER','USERLOG'),
    ('PAY','PAYLOG'),
    ('BIZ','BIZLOG'),
    ('ADMIN','ADMINLOG'),
    ('ALIBBLIFE','ALIBBLIFELOG'),
    ('COMM','COMMLOG'),
    ('CONFIG','CONFIGLOG'),
    ('MOBILE','MOBILELOG'),
    ('ORDER','OADERLOG'),
    ('PROMOTION','PROMOTIONLOG'),
    ('SHOP','SHOPLOG'),
    ('WAP','WAPLOG'),
    ('WX','WXLOG'),
)


# Create your models here.

class RemoteBizInfo94(models.Model):
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class RemoteBizError94(models.Model):
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class RemoteBizInfo98(models.Model):
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class RemoteBizError98(models.Model):
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content



class LogMonitor(models.Model):
    log_type = models.CharField(max_length=100,choices=TYPE_CHOICES)
    log_path = models.CharField(max_length=500)
    timing = models.IntegerField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.log_type


class UserLogSystem(models.Model):
    # log_type = models.ForeignKey(LogMonitor,on_delete=models.CASCADE)
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:225]+'...'


class UserLogWarning(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class UserLogError(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class UserLogInfo(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class LogLevel(models.Model):
    level = models.CharField(max_length=225)
    desc = models.CharField(max_length=225)
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.level


class BizServiceError(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class AdminWebError(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


# class AlibblifeWebError(models.Model):
#     log_type = models.CharField(max_length=225)
#     log_level = models.CharField(max_length=225)
#     content = models.TextField()
#     create_time = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.content


class AlilifeServiceError(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class CommunicationServiceError(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class ConfigServiceError(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class MobileWebError(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class OrderServiceError(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class PayServiceError(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class PromotionServiceError(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class ShopServiceError(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class UserServiceError(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class WapWebError(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class WxServiceError(models.Model):
    log_type = models.CharField(max_length=225)
    log_level = models.CharField(max_length=225)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class SshConfig(models.Model):
    hostname = models.CharField(max_length=225)
    port = models.IntegerField()
    username = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.hostname




