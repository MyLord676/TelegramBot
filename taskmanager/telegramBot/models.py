from django.db import models


class Notify(models.Model):
    tg_id = models.IntegerField()
    notify_text = models.TextField(blank=True, null=True)
    sended = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'notify'


class Requests(models.Model):
    tg_id = models.IntegerField()
    ts = models.DateTimeField()
    request_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requests'


class Users(models.Model):
    create_dt = models.DateTimeField()
    tg_id = models.IntegerField()
    username = models.TextField(blank=True, null=True)
    descrtext = models.TextField(blank=True, null=True)
    first_token = models.TextField(blank=True, null=True)
    token_requests_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'
