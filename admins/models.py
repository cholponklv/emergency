from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


# Create your models here.


class MyCustomUserManger(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email must be exist')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_admin', True) is not True:
            raise ValueError('Admin must have is_admin=True.')

        return self.create_user(email, password, **extra_fields)


class Admin(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyCustomUserManger()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username
