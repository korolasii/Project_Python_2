from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content_preview = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Category(models.Model):
    name = models.CharField(max_length=255)