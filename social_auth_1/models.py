from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


class Account(models.Model):
    id = models.AutoField(primary_key = True)
    avatar = models.ImageField(upload_to='static')

    first_name = models.TextField()
    second_name = models.TextField()
    third_name = models.TextField()

    about_you = models.TextField()

    user = models.OneToOneField(User, on_delete=models.CASCADE)
