from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} - {self.address}'

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images", null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'

