from django.db import models

# Create your models here.
class Certif(models.Model):
    Name = models.CharField(max_length=100)
    Img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.Name

class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Message = models.TextField()

    def __str__(self):
        return self.Name