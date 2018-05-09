from django.test import TestCase
from django.urls import reverse
from ..models import User


class LoginTestCase(TestCase):

    def setUp(self):
        # Apparently this does not work. I don't really know why
        # I assume the reason this is not working is the fact that django encrypts the password
        # User.objects.create(email='admin@test.com',
        #                     password='admin1234',
        #                     first_name='Admin',
        #                     last_name='Test',
        #                     phone_number='0730123456')
        self.credentials = {
            'email': 'admin@test.com',
            'password': 'admin1234',
            'first_name': 'Admin',
            'last_name': 'Test',
            'phone_number': '0730123456'
        }

        User.objects.create_user(**self.credentials)

    def test_login_returns_200(self):
        # listings = Listing.objects.all()
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_returns_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login_template.html')

    def test_login_user_with_error(self):
        # user = User.objects.first()
        response = response = self.client.post(reverse('login'),
                                               {'email': 'test@email.com', 'password': 'somepass'},
                                               follow=True)

        assert 'error' in response.context

    def test_login_user(self):
        # user = User.objects.first()
        response = response = self.client.post(reverse('login'),
                                               {'email': 'admin@test.com', 'password': 'admin1234'},
                                               follow=True)

        assert 'error' not in response.context
        # print(response.context['error'])
        self.assertEqual(response.status_code, 200)

        # This check is enough. The ListListingsTestCase checks for template
        self.assertRedirects(response, reverse('list_listings'))
        # self.assertTemplateUsed(response, 'list_listings_template.html')
