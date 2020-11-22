"""
Test to see if each view is correct
"""
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from ..views import home


class TestViews(TestCase):

    # test for the homepage
    def test_home_view(self):
        client = Client()
        response = client.get(reverse(home))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html', 'base.html')

    # tests both the "logged in" and "logged out" views;
    # creates a test user, logs them in, ensures "logged in" view shown
    # then, logs the user out and ensures "logged out" view is shown
    def test_user_home_view(self):
        client = Client()
        User.objects.create_user(username="testUser", password="t3stp4ss")
        loggedIn = client.login(username='testUser', password='t3stp4ss')
        self.assertEquals(loggedIn, True)
        response = client.get(reverse(home))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/user_home.html', 'base.html')
        client.logout()
        response = client.get(reverse(home))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html', 'base.html')

