from django.db import models


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} - {self.address}'


class Participant(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.email}'


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organiser_email = models.EmailField(null=True)
    date = models.DateField(null=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images", null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    participants = models.ManyToManyField(Participant, blank=True)

    def __str__(self):
        return f'{self.title}'
