from django.db import models
from django.urls import reverse
import unicodedata
# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length = 50, null = False, unique = True)
    introduction = models.TextField()

    def get_normalize_name(self):
        return ''.join(c for c in unicodedata.normalize('NFD', self.name) if unicodedata.category(c) != 'Mn').lower().replace(' ', '-')

    def __str__(self):
        return self.get_normalize_name()
    def get_absolute_url(self):
        return reverse('region-detail', args=[self.get_normalize_name()])

class City(models.Model):
    name = models.CharField(max_length = 50, null = False, unique = True)
    region = models.ForeignKey(Region, on_delete=models.RESTRICT, null = True)
    introduction = models.TextField()
    weather = models.TextField()
    transport = models.TextField()

    def get_upload_path(self, filename):
        return "%s/%s/%s" % (self.get_normalize_name(),self.get_normalize_name(), filename)

    banner = models.FileField(upload_to=get_upload_path)

    def get_normalize_name(self):
        return ''.join(c for c in unicodedata.normalize('NFD', self.name) if unicodedata.category(c) != 'Mn').lower().replace(' ', '-')

    def __str__(self):
        return self.get_normalize_name()
    
    def get_absolute_url(self):
        return reverse('city-detail', args=[self.region.get_normalize_name(),self.get_normalize_name()])
    
class CityGallery(models.Model):
    city = models.ForeignKey(City, on_delete=models.RESTRICT)

    def get_upload_path(self, filename):
        return "%s/%s/%s" % (self.city.get_normalize_name(),self.city.get_normalize_name(), filename)

    image = models.FileField(upload_to=get_upload_path)

class Category(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return ''.join(c for c in unicodedata.normalize('NFD', self.name) if unicodedata.category(c) != 'Mn').lower().replace(' ', '-')

class Destination(models.Model):
    name = models.CharField(max_length = 150, null = False)
    city = models.ForeignKey(City, on_delete=models.RESTRICT, null = True)
    location = models.CharField(max_length = 500, null = True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, null = True)

    description = models.TextField()

    def get_upload_path(self, filename):
        return "%s/%s/%s" % (self.city.get_normalize_name(),self.get_normalize_name(), filename)

    banner = models.FileField(upload_to=get_upload_path)

    def get_normalize_name(self):
        return ''.join(c for c in unicodedata.normalize('NFD', self.name) if unicodedata.category(c) != 'Mn').lower().replace(' ', '-')

    def __str__(self):
        return self.get_normalize_name()
    
    def get_absolute_url(self):
        return reverse('destination-detail', args=[self.city.region.get_normalize_name(),self.city.get_normalize_name(),self.get_normalize_name()])
    
class DestinationGallery(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.RESTRICT)

    def get_upload_path(self, filename):
        return "%s/%s/%s" % (self.destination.city.get_normalize_name(),self.destination.get_normalize_name(), filename)

    image = models.FileField(upload_to=get_upload_path)
