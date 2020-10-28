"""
Test to see if each url can be resolved
"""

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import register


# Test to see if each url can be resolved
class TestUrls(SimpleTestCase):

    # test for the register page
    def test_register_url(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)
