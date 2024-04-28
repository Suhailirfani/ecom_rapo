from django.test import TestCase
from django.urls import resolve , reverse
from shop.models import *

class TestModel(TestCase):
    def test_category(self):
        category1 = Category.objects.create(name='Home and living', slug='home', desc='demo')
        self.assertEqual(str(category1), 'Home and living')
        self.assertTrue(isinstance(category1, Category))