"""
Test to see if each url can be resolved
"""

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import home


class TestUrls(SimpleTestCase):

    # test for the homepage
    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
