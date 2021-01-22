'''
  makemigrations
  migrate50

'''
from django.db import models

class airport(models.Model):
    city=models.CharField(max_length=60)
    code=models.CharField(max_length=50)

    def __str__(self):
        return f"Airport({self.city},{self.code})"

# Create your models here.
class flights(models.Model):
    origin=models.ForeignKey('airport',on_delete=models.CASCADE,related_name='arrival')
    destions=models.ForeignKey('airport',on_delete=models.CASCADE,related_name='departure')
    durations=models.IntegerField()

    def __str__(self):
        return f"flight(origin:{self.origin} , destions={self.destions})"

class passenger(models.Model):
    first_name=models.CharField(max_length=55)
    last_name=models.CharField(max_length=55)
    planes=models.ManyToManyField(flights,related_name='passengers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}";



