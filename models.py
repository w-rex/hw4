from django.db import models

# Create your models here.

class Student(models.Model):
    objects = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    major = models.CharField(max_length=100)
    direction = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=5)

class Blog(models.Model):
    image = models.ImageField(upload_to="blog_pics/")
    title = models.CharField(max_length=50)
    description = models.CharField(min_length=1)
    hashtags = models.TextField()