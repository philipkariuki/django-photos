from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Image,Category,Location,tags
import datetime as dt




class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new editor and saving it
        self.kagura= Image(name = 'Kagura Mikazuchi', description ='Kagura is a badass master of the sword',location= 'self.fairy tail', category= 'anime', article_image='images/kagura.png')
        self.kagura.save_image()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'anime')
        self.new_tag.save()

        self.new_image= Article(name = 'Test Image',description = 'This is a random test image description',location = self.kagura)
        self.new_image.save()

        self.new_article.tags.add(self.new_tag)
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kagura,Image))


    # Testing new article
    def test_new_image(self):
        self.new_image= Image(name = 'Test Image',description = 'This is a random test image description',location = self.kagura)
        self.new_image.save()
        
    # Testing  new tag
    def test_new_tag(self):
        self.new_tag = tags(name = 'anime')
        self.new_tag.save()


    def tearDown(self):
        Image.objects.all().delete()
        tags.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
        
    
class TagTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kagura= tags( name = 'anime' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kagura,tags))
        
    # Testing Save Method
    def test_save_method(self):
        self.kagura.save_tag()


class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kagura= Location( location_name = 'fairy tail' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kagura,Location))
        
    # Testing Save Method
    def test_save_method(self):
        self.kagura.save_location()

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kagura= Category( category_name = 'anime' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kagura,Category))
        
    # Testing Save Method
    def test_save_method(self):
        self.kagura.save_category()