"""
Test to see if each view is correct
"""

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from ..views import register, login


# Test to see if each view is correct
class TestViews(TestCase):

    # test for the register page
    # a logged in user should not see the register page
    # a logged out user should be able to see the register page
    def test_register_view(self):
        client = Client()
        User.objects.create_user(username="testUser", password="t3stp4ss")
        loggedIn = client.login(username='testUser', password='t3stp4ss')
        self.assertEquals(loggedIn, True)
        response = client.get(reverse(register))
        self.assertNotEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html', 'base.html')
        client.logout()
        response = client.get(reverse(register))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html', 'base.html')

    # test for the login page
    # a logged in user should not see the login page
    # a logged out user should be able to see the login page
    def test_login_view(self):
        client = Client()
        User.objects.create_user(username="testUser", password="t3stp4ss")
        loggedIn = client.login(username='testUser', password='t3stp4ss')
        self.assertEquals(loggedIn, True)
        response = client.get(reverse(login))
        self.assertNotEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html', 'base.html')
        client.logout()
        response = client.get(reverse(login))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html', 'base.html')
