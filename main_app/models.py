from django.db import models
from django.urls import reverse


class Wish(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wish_list')