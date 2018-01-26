from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField()
    # add in thumbnail later
    # add in author later
    def __init__(self):
        pass
