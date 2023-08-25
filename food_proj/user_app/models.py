from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Client(AbstractUser):
    username = models.CharField(
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', 
        max_length=150, 
        unique=True, 
        verbose_name='username')
    # name = models.CharField(
    #     max_length=240, 
    #     verbose_name='Name')
    
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    
    
    REQUIRED_FIELDS = []

    # def __str__(self):
    #     return self.name