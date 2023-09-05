from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

GENDER_CHOICES = (("M","Male"), ("F", "Female"), ("", "Do not wish to disclose") )

class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='profile images', default='image.png')
    age = models.PositiveIntegerField(default='18', null=True, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default="M", null=True, blank=True)
    class Meta:
        verbose_name_plural = 'User'
    
    def __str__(self):
        return self.username
    
    REQUIRED_FIELDS =[]
    USERNAME_FIELD = 'email'
    