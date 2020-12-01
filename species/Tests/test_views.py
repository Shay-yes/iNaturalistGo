from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from ..views import submit_view, gallery_view

class TestViews(TestCase):
    # ensure gallery view uses correct templates
    def test_gallery_view(self):
        client = Client()
        User.objects.create_user(username="testUser", password="t3stp4ss")
        loggedIn = client.login(username='testUser', password='t3stp4ss')
        self.assertEquals(loggedIn, True)
        response = client.get(reverse(gallery_view))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'species/gallery.html', 'base.html')

    # ensures "species upload" view uses correct templates
    def test_submit_view(self):
        client = Client()
        User.objects.create_user(username="testUser", password="t3stp4ss")
        loggedIn = client.login(username='testUser', password='t3stp4ss')
        self.assertEquals(loggedIn, True)
        response = client.get(reverse(submit_view))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'species/species_form.html', 'base.html')