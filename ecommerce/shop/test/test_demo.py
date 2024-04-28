from django.test import TestCase

# Create your tests here.
def concate_strings(str1,str2):
    return str1 + str2

class TestDemo(TestCase):
    def test_concate(self):
        self.assertEqual(concate_strings('hello ', 'how are you') , 'hello howe are you')