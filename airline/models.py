'''
  makemigrations
  migrate

'''
from django.db import models

# Create your models here.
class flights(models.Model):
    origin=models.CharField(max_length=50)
    destions=models.CharField(max_length=50)
    durations=models.IntegerField()

    def __str__(self):
        return f"flight(origin:{self.origin} , destions={self.destions})"

