from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class AdminManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("The Username field is required.")
        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user

class Admin(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    objects = AdminManager()

    USERNAME_FIELD = 'username'

