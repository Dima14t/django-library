from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.CharField(max_length=100, verbose_name='Автор')
    published_date = models.CharField(verbose_name='Дата издания')
    isbn = models.CharField(max_length=13, blank=True, verbose_name='ISBN')
    pages = models.CharField(verbose_name='Количество страниц')

    def __str__(self):
        return f"{self.title} by {self.author}"

