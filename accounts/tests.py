from django.test import TestCase
from django.urls import reverse, resolve
from . import views
# Create your tests here.

class signupTest(TestCase):
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_resolver_signup_view(self):
        view = resolve(reverse('signup'))
        # self.assertEquals(view.func, views.signup)
        self.assertEquals(view.func, views.signup.as_view())
