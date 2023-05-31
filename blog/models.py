from django.db import models

# Create your models here.

class Article(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='articles', default=1, verbose_name='Категорія')
    tags = models.ManyToManyField('Tag', related_name='articles', verbose_name='Теги')
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content_preview = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(verbose_name='URL', default='')
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
