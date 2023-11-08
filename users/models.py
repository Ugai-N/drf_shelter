from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _ # для автоматического перевода всего что после _

from shelter.models import NULLABLE


class User(AbstractUser):
    FREQUENCY_CHOICES = [
        ('member', _('member')),
        ('moderator', _('moderator'))
    ]
    username = None
    email = models.CharField(verbose_name='email', unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    phone = models.CharField(verbose_name='телефон', max_length=35, **NULLABLE)
    telegram = models.CharField(verbose_name='телеграм ник', max_length=50, **NULLABLE)
    avatar = models.ImageField(verbose_name='аватар', upload_to='users/', **NULLABLE)
    age = models.PositiveIntegerField(**NULLABLE)
    role = models.CharField(max_length=150, choices=FREQUENCY_CHOICES, verbose_name='роль', default='member')
