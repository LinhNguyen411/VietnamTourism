from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
import unicodedata
import re
# Create your models here.

TABLE = str.maketrans(
    "ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÈÉẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴáàảãạăắằẳẵặâấầẩẫậđèéẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ",
    "A"*17 + "D" + "E"*11 + "I"*5 + "O"*17 + "U"*11 + "Y"*5 + "a"*17 + "d" + "e"*11 + "i"*5 + "o"*17 + "u"*11 + "y"*5
)

def normalize(txt: str) -> str:
    if not unicodedata.is_normalized("NFC", txt):
        txt = unicodedata.normalize("NFC", txt)
    return txt.translate(TABLE)

class Region(models.Model):
    name = models.CharField(max_length = 50, null = False, unique = True)
    introduction = models.TextField()

    banner = models.FileField(upload_to='regions/')

    def get_normalize_name(self):
        return '-'.join(re.findall(r'\w+', normalize(self.name))).lower()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('region-detail', args=[self.get_normalize_name()])
    
    class Meta:
        ordering = ('id',)

class City(models.Model):
    name = models.CharField(max_length = 50, null = False, unique = True)
    
    region = models.ForeignKey(Region, on_delete=models.RESTRICT, null = True)
    introduction = models.TextField()
    weather = models.TextField()

    transport = models.TextField()

    def transport_lines(self):
        return filter(None, (line.strip() for line in self.transport.splitlines()))

    def get_upload_path(self, filename):
        return "%s/%s/%s" % (self.get_normalize_name(),self.get_normalize_name(), filename)

    banner = models.FileField(upload_to=get_upload_path)

    def get_normalize_name(self):
        return '-'.join(re.findall(r'\w+', normalize(self.name))).lower()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('city-detail', args=[self.region.get_normalize_name(),self.get_normalize_name()])
    
    class Meta:
        ordering = ('id',)
    
class CityGallery(models.Model):
    city = models.ForeignKey(City, on_delete=models.RESTRICT)

    def get_upload_path(self, filename):
        return "%s/%s/%s" % (self.city.get_normalize_name(),self.city.get_normalize_name(), filename)

    image = models.FileField(upload_to=get_upload_path)

class Category(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

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
        return '-'.join(re.findall(r'\w+', normalize(self.name))).lower()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('destination-detail', args=[self.city.region.get_normalize_name(),self.city.get_normalize_name(),self.get_normalize_name()])
    
class DestinationGallery(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.RESTRICT)

    def get_upload_path(self, filename):
        return "%s/%s/%s" % (self.destination.city.get_normalize_name(),self.destination.get_normalize_name(), filename)

    image = models.FileField(upload_to=get_upload_path)