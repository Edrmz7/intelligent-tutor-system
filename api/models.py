from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    examen = models.BooleanField(default=False)
    level = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email

class Exam(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

class Tutor (models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.TextField()   
    date_created = models.DateTimeField(auto_now_add=True) 



