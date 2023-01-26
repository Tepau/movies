from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    cover = models.ImageField(upload_to='covers')
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name

