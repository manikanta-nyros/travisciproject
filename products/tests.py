from django.test import TestCase

# Create your tests here.
from django.test import TestCase

class AirthmeticTestCase(TestCase):
    def setUp(self):
        self.a = 10
        self.b = 20

    def test_addition(self):
        """ADD two digits"""
        c = self.a+self.b
        print c
        self.assertEqual(c, 30)
    def test_sub(self):
        c = self.a-self.b
        print c
        self.assertEqual(c,30)