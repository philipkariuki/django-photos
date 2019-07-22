from django.contrib import admin
from .models import Location,Image,tags, Category

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Location)
admin.site.register(Image, ImageAdmin)
admin.site.register(Category)
admin.site.register(tags)
