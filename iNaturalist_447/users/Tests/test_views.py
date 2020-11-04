"""
Test to see if each view is correct
"""

from django.test import TestCase, Client
from django.urls import reverse
from ..views import register, login


# Test to see if each view is correct
class TestViews(TestCase):

    # test for the register page
    def test_register_view(self):
        client = Client()
        response = client.get(reverse(register))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html', 'base.html')

    # test for the register page
    def test_login_view(self):
        client = Client()
        response = client.get(reverse(login))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html', 'base.html')
