"""
Test to see if each form is working correctly
"""


from django.test import SimpleTestCase, TestCase
from ..forms import UserRegisterForm, UserLoginForm


class TestForms(TestCase):

    # test for valid register page inputs
    def test_register_form_valid(self):
        form = UserRegisterForm(data={
            'username': 'DudeMan123',
            'email': 'dude@man.com',
            'password1': 't3stp4ss',
            'password2': 't3stp4ss'
        })

        self.assertTrue(form.is_valid())

    # test for valid register page inputs
    def test_register_form_invalid(self):
        form = UserRegisterForm(data={
            'username': '/',
            'email': '/',
            'password1': '|',
            'password2': '/'
        })

        self.assertFalse(form.is_valid())

    # test for empty register page inputs
    def test_register_form_empty(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    # test for valid login page inputs
    def test_login_form_valid(self):
        form = UserLoginForm(data={
            'user_name': 'testymctestface',
            'pass_word': 't3st1ng!'
        })

        self.assertTrue(form.is_valid())

    # test for invalid login page inputs
    def test_login_form_invalid(self):
        form = UserLoginForm(data={
            'user_name': '/',
            'pass_word': 'poidfugposiudfgpoisudfpgoiusdpfiogupsdfuposudfgposiudfpgoiuspfiogupsdfugpsdgfupdgfupsodgfupoisudfgpgspdo'
        })

        self.assertFalse(form.is_valid())

    # test for empty login page inputs
    def test_login_form_empty(self):
        form = UserLoginForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
