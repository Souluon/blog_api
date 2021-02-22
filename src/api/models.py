from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Тэги')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Тэги'
        verbose_name_plural = 'Тэги'

class Post(models.Model):
    title = models.CharField(max_length = 100, verbose_name = 'Заголовок')
    body = models.TextField(max_length = 1000, verbose_name = 'Описание')

    tags = models.ManyToManyField(Tag, related_name = 'posts', verbose_name = 'Тэги')
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
