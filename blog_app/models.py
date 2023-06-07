from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Recipe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name