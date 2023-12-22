from django.contrib import admin
from .models import Region, City, CityGallery, Category, Destination, DestinationGallery
# Register your models here.
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Region, RegionAdmin)

class CityGalleryInline(admin.TabularInline):
    model = CityGallery

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
    list_filter = ('region',)
    inlines = [CityGalleryInline]

admin.site.register(City, CityAdmin)

admin.site.register(CityGallery)

admin.site.register(Category)

class DestinationGalleryInline(admin.TabularInline):
    model = DestinationGallery

class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    list_filter = ('category',)
    inlines = [DestinationGalleryInline]

admin.site.register(Destination, DestinationAdmin)
admin.site.register(DestinationGallery)