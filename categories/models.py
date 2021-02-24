from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    
    def __str__(self):
        return f'name - {self.name}'
