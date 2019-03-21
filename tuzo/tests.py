from django.test import TestCase
from .models import *
# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):

        self.image= Image(name = 'black',caption ='image of a black man')
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    def tearDown(self):
        Image.objects.all().delete()
