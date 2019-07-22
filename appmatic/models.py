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
    description = models.TextField(max_length =35)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    article_image = models.ImageField(upload_to = 'articles/')


    def __str__(self):
        return self.title


    @classmethod
    def search_by_title(cls,search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos


