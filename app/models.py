from django.db import models
from .random_generator import random_personal_id
# Create your models here.
class Link(models.Model):
    link = models.CharField(max_length=255, verbose_name="Ссылка")
    personal_id = models.CharField(max_length=255, verbose_name="Уникальный id")

    def save(self,*args,**kwargs):
        if not self.personal_id:
            self.personal_id = random_personal_id()
        super().save(*args,*kwargs)

    def Meta(self):
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return self.link