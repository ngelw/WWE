from django.db import models

# Create your models here.
class Wrestlers(models.Model):
    name = models.CharField(max_length=55)
    weight=models.IntegerField()
    height = models.FloatField()
    signature = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name