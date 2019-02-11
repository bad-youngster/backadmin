from django.db import models


class registra(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    verfiypassword = models.CharField(max_length=20)
    registratime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['registratime']
        verbose_name = 'email'
        verbose_name_plural = 'email'

class UserModels(models.Model):
    username = models.CharField(max_length=6)
    password = models.CharField(max_length=20)
    regtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['regtime']
        verbose_name = 'username'
        verbose_name_plural = 'username'

class LoginModels(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
