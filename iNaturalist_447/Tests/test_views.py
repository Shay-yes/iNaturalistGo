"""
Test to see if each view is correct
"""

from django.test import TestCase, Client
from django.urls import reverse
from ..views import home


class TestViews(TestCase):

    # test for the homepage
    def test_home_view(self):
        client = Client()
        response = client.get(reverse(home))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html', 'base.html')
