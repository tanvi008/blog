from django.test import TestCase
from .models import *
from faker import Faker

fake=Faker()

class FirstTestCase(TestCase):

    def setup(self):
        print("my first test case")


    def test_blog_category(self):
        pass


