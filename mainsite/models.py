from django.db import models

from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title
class companyplace(models.Model):
    City_place = models.CharField(max_length=1000, null=False)
    City_number = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return self.City_place

class company(models.Model):
    time = models.CharField(max_length=1000, null=False)
    place = models.CharField(max_length=1000, default='M', null=False)
    dead = models.CharField(max_length=1000, default='M', null=False)
    Injured = models.CharField(max_length=1000, default='M', null=False)
    car = models.CharField(max_length=1000, blank=True, default='')
    longitude = models.CharField(max_length=1000, blank=True, default='')
    latitude = models.CharField(max_length=1000, blank=True, default='')
    def __str__(self):
        return self.time


