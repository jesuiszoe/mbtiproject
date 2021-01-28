from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    pass


# Create your models here.
class Signup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
