from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year_publishing = models.DateField()
    description = models.TextField()
    cover_image = models.ImageField()


class Author(models.Model):
    name = models.CharField(max_length=100)
    date_birth = models.DateField()
    biography = models.TextField()


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.name} Profile'

    birth_date = models.DateField(null=True, blank=True)
