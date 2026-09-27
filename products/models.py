from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):

    def create_user(self, mobile, password=None, **extra_fields):
        if not mobile:
            raise ValueError('Phone number is required')

        user = self.model(
            mobile=mobile,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, mobile, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(
            mobile=mobile,
            password=password,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):

    mobile = models.CharField(max_length=11, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    create_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "mobile"

    def __str__(self):
        return self.mobile