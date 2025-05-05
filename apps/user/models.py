from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, username, password, name,lastname, **extra_fields):
        user = self.model(
            username = username,
            name = name,
            lastname = lastname, 
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, name, lastname, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        return self._create_user(username, password, name, lastname, **extra_fields)

    def create_superuser(self, username, name, lastname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, password, name, lastname, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    COORDINATION = 1 
    ADMIN = 2
    ENGINEER_BIOMEDICAL = 3
    ACCOUNTANT = 4
    ROLE_CHOICES = (
        (COORDINATION, 'coordination'),
        (ENGINEER_BIOMEDICAL, 'biomedical'),
        (ADMIN, 'admin'),
        (ACCOUNTANT, 'accountant'),
    )

    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=100, unique=True)
    token_password = models.CharField(null=True, blank=True,max_length = 50,unique = True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    rol = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','lastname','rol']

    def __str__(self):
        return f'{self.name} {self.lastname}'