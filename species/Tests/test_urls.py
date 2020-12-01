from django.test import TestCase, Client
from django.urls import reverse, resolve
from ..views import gallery_view, submit_view
from django.contrib.auth.models import User

class TestUrls(TestCase):

    # test for the "gallery page" url
    def test_gallery_url(self):
        url = reverse(gallery_view)
        self.assertEquals(resolve(url).func, gallery_view)
    
    # test to see if the "species upload" url works for signed-in users
    def test_upload_url(self):
        client = Client()
        User.objects.create_user(username="testUser", password="t3stp4ss")
        loggedIn = client.login(username='testUser', password='t3stp4ss')
        self.assertEquals(loggedIn, True)
        url = reverse(submit_view)
        self.assertEqual(resolve(url).func, submit_view)
        client.logout()