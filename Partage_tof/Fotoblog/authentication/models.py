from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Createur'),
        (SUBSCRIBER, 'Abonné'),

    )
    profile_photo = models.ImageField(verbose_name='Photo_de_profile')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Role')

