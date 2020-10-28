"""
Test to see if each form is working correctly
"""


from django.test import SimpleTestCase, TestCase
from ..forms import UserRegisterForm


class TestForms(TestCase):

    def test_register_form_valid(self):
        form = UserRegisterForm(data={
            'username': 'DudeMan123',
            'email': 'dude@man.com',
            'password1': 'pass123',
            'password2': 'pass123'
        })

        self.assertTrue(form.is_valid())

    def test_register_form_empty(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
