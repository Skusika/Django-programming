from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(3)])
    surname = models.CharField(max_length=40)
    feedback = models.TextField()
    rating = models.PositiveIntegerField()
