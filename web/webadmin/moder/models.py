from django.db import models


class TgUser(models.Model):
    tg_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    lower_name = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=500, unique=True)
    cart = models.CharField(max_length=100, blank=True)
    traffic = models.TextField(blank=True)
    discount = models.TextField(blank=True)
    bonus = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return f'{self.name}' if self.name else "Пользователь не авторизован"


class Info(models.Model):
    title = models.TextField()
    article = models.TextField()


class Message(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()


class Moder(models.Model):
    tg_id = models.CharField(max_length=500)
