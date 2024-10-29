from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Wrestlers(models.Model):
    name = models.CharField(max_length=55)
    weight=models.IntegerField()
    height = models.FloatField()
    signature = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='wrestler',null=True,unique=False)

    def __str__(self):
        return self.name