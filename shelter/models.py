from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Dog(models.Model):
    name = models.CharField(max_length=250, verbose_name='кличка')
    photo = models.ImageField(upload_to='photo/', verbose_name='фото', **NULLABLE)
    birth = models.DateField(verbose_name='ДР', **NULLABLE)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, verbose_name="порода", related_name='dog', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="автор", **NULLABLE)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'
        ordering = ('name', 'author',)


class Parent(models.Model):
    name = models.CharField(max_length=250, verbose_name='кличка')
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, verbose_name="порода", **NULLABLE)
    dog = models.ForeignKey('Dog', on_delete=models.CASCADE, verbose_name='собака')
    birth = models.DateField(verbose_name='ДР', **NULLABLE)

    def __str__(self):
        return f'{self.name} (предок {self.dog})'

    class Meta:
        verbose_name = 'предок'
        verbose_name_plural = 'предки'


class Breed(models.Model):
    breed = models.CharField(max_length=250, verbose_name='порода')
    description = models.CharField(max_length=250, verbose_name='Описание', **NULLABLE)
    pic = models.ImageField(upload_to='pics/', verbose_name='Картинка', **NULLABLE)

    def __str__(self):
        return f'{self.breed}'

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'
