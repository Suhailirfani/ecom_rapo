from django.test import TestCase

# Create your tests here.
class test_url(TestCase):
    def test_home(self):
        result = self.client.get('/payments/')
        self.assertEqual(result.status_code, 200)