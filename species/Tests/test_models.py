from django.test import TestCase, Client
from django.urls import reverse
from django.db import migrations, models
from django.contrib.auth.models import User
from species.models import Species


# tests for the Species model
class TestSpecies(TestCase):

    def test_valid_common_name(self):
        test_man = User.objects.create_user(username="testUser", password="t3stp4ss")
        test_specie = Species(user=test_man, common_name="THE NAME", latin_name="LATIN")
        self.assertEquals(test_specie.__str__(), "THE NAME")

    def test_invalid_common_name(self):
        test_man = User.objects.create_user(username="testUser", password="t3stp4ss")
        test_specie = Species(user=test_man, common_name="THE NAME", latin_name="LATIN")
        self.assertNotEqual(test_specie.__str__(), "THEEEE NAME")


