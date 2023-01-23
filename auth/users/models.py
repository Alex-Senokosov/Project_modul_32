from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import  CharField

class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique = True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

# Create your models here.
