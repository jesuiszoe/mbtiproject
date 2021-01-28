from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Signup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
class Post(models.Model):  
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    mbti = models.TextField()

    def __str__(self):
        return self.title