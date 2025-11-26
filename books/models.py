from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20)  # Use CharField for ISBN
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title