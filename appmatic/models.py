from django.db import models
import datetime as dt

# Create your models here.
        
        
class tags(models.Model):
    name = models.CharField(max_length =30)

    def save_tag(self):
        self.save()

    def __str__(self):
        return self.name        
        
        
class Image(models.Model):
    name = models.CharField(max_length =25)
    description = models.TextField(max_length =850)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    article_image = models.ImageField(upload_to = 'images/')
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



    @classmethod
    def new_images(cls):
        photoz = Image.objects.all()
        return photoz


    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__category_name__icontains=search_term)
        return photos




class Location(models.Model):
    location_name = models.CharField(max_length =30)
    
    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    class Meta:
        ordering = ['location_name']

class Category(models.Model):
    category_name = models.CharField(max_length =30)
    
    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    class Meta:
        ordering = ['category_name']


