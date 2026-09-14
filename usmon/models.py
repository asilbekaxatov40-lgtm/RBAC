from django.db import models
# from app.models import CustomUser

class Book(models.Model):
    title = models.CharField(max_length=150)
    owner = models.ForeignKey('app.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.title