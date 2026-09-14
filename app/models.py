from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOISE = [
        ('Student', 'Oquvchi'),
        ('Teacher', 'Oqituvchi'),
    ]
    role = models.CharField(max_length=150, choices=ROLE_CHOISE)
    phone = models.CharField(max_length=150)

    def __str__(self):
        return self.username