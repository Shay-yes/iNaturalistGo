"""
Test to see if each view is correct
"""

from django.test import TestCase, Client
from django.urls import reverse
from ..views import register


# Test to see if each view is correct
class TestViews(TestCase):

    # test for the register page
    def test_register_view(self):
        client = Client()
        response = client.get(reverse(register))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
