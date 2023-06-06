from django.db import models

# Create your models here.

class Article(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    STATUS_CHOICES = (
        (ACTIVE, 'Активна'),
        (DRAFT, 'Чернетка'),
    )
    
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='articles', default=1, verbose_name='Категорія')
    tags = models.ManyToManyField('Tag', related_name='articles', verbose_name='Теги')
    title = models.CharField(max_length=255, verbose_name="Заголовок", unique=True)
    slug = models.SlugField(verbose_name="URL", unique=True)
    content_preview = models.TextField(verbose_name="Текст preview")
    content = models.TextField(verbose_name="Основной текст")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DRAFT, verbose_name='Статус')
    image = models.ImageField(upload_to='articles/', verbose_name='Зображення', blank=True, null=True)
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
    
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва Категорії', unique=True)
    slug = models.SlugField(verbose_name='URL', default='', unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва тегу', unique=True)
    slug = models.SlugField(verbose_name='URL', default='', unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255, verbose_name='Ім\'я')
    email = models.EmailField(verbose_name='Email')
    content = models.TextField(verbose_name='Коментар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')

    def __str__(self):
        return f'{self.article.title} - {self.content}'
    
    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ['-created_at']
    
    
    def __str__(self):
        return f'{self.article.title} - {self.content}'