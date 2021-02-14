from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.id])


class BookUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    phone_no = models.IntegerField(null=True, blank=True)


