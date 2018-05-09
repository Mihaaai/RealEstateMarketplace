from django.test import TestCase
from django.urls import reverse
from ..models import User


class RegisterTestCase(TestCase):

    def setUp(self):
        self.credentials = {
            'email': 'admin@test.com',
            'first_name': 'Admin',
            'last_name': 'Test',
            'phone_number': '0730123456',
            'password1': 'q8isx1$7@',
            'password2': 'q8isx1$7@'
        }

    def test_register_returns_200(self):
        # listings = Listing.objects.all()
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_login_returns_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'register_template.html')

    # def test_login_user_with_error(self):
    #     # user = User.objects.first()
    #     response = response = self.client.post(reverse('login'),
    #                                            {'email': 'test@email.com', 'password': 'somepass'},
    #                                            follow=True)

    #     assert 'error' in response.context

    def test_register_user(self):
        # user = User.objects.first()
        response = response = self.client.post(reverse('register'),
                                               self.credentials,
                                               follow=True)

        self.assertEqual(response.status_code, 200)

        # This check is enough. The ListListingsTestCase checks for template
        # self.assertRedirects(response, reverse('homepage'))
        self.assertTemplateUsed(response, 'template.html')

        # In order to check that the account has been created, we have to make a login.
        self.login_user()

    def login_user(self):
        # user = User.objects.first()
        response = response = self.client.post(reverse('login'),
                                               {'email': 'admin@test.com', 'password': 'q8isx1$7@'},
                                               follow=True)

        # assert 'error' in response.context
        # print(response.context['error'])
        self.assertEqual(response.status_code, 200)

        # This check is enough. The ListListingsTestCase checks for template
        self.assertRedirects(response, reverse('list_listings'))
        # self.assertTemplateUsed(response, 'list_listings_template.html')
