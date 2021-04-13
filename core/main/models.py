from django.db import models
from django.shortcuts import reverse


class Team(models.Model):
    name_team = models.CharField(max_length=50, db_index=True)
    image_team = models.ImageField(upload_to='main/media/image_team')
    image_car = models.ImageField(upload_to='main/media/car_team')
    pilot1 = models.CharField(max_length=50, db_index=True)
    pilot2 = models.CharField(max_length=50, db_index=True)
    age1 = models.IntegerField(default=0)
    age2 = models.IntegerField(default=0)
    birthday1 = models.CharField(max_length=30, db_index=True)
    birthday2 = models.CharField(max_length=30, db_index=True)
    body = models.TextField(blank=True, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)


    def get_absolute_url(self):
        return reverse('teams_detail_url', kwargs={'slug': self.slug})


    def __str__(self):
        return self.name_team

    # def get_absolute_url(self, request):

class Gallery(models.Model):
    name_image = models.CharField(max_length=50, db_index=True)
    image = models.ImageField(upload_to='main/media/gallery')

    def __str__(self):
        return '{}'.format(self.name_image)

class Feedback(models.Model):
    firstname = models.CharField(max_length=50, db_index=True)
    lastname = models.CharField(max_length=60, db_index=True)
    email = models.EmailField(db_index=True)
    message = models.TextField(blank=True, db_index=True)
    response = models.BooleanField(default=False)

