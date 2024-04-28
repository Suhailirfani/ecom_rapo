from django.test import TestCase
from django.urls import resolve , reverse
from shop.views import *

class TestUrl(TestCase):
    def test_home(self):
        url= reverse('home')
        print('url is ', url)
        self.assertEqual(resolve(url).func, home)
        self.assertTemplateUsed('home.html')
        print(resolve(url))