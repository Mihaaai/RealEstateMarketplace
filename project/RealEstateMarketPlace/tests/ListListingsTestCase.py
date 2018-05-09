from django.test import TestCase
from django.urls import reverse
from ..models import Listing, Estate, User

# You run this test like this:
# python3 manage.py test RealEstateMarketPlace.tests.ListListingsTestCase
# All tests can be run using:
# python3 manage.py test RealEstateMarketPlace.tests


class ListListingsTestCase(TestCase):

    def setUp(self):
        user1 = User.objects.create(email='admin@test.com',
                                    password='admin1234',
                                    first_name='Admin',
                                    last_name='Test',
                                    phone_number='0730123456')
        user2 = User.objects.create(email='admin2@test.com',
                                    password='admin4321',
                                    first_name='Admin2',
                                    last_name='Test2',
                                    phone_number='0730123457')
        estate1 = Estate.objects.create(address='strada Voievozilor nr. 15',
                                        price=78123,
                                        rooms=4,
                                        floor=3,
                                        size=150,
                                        year=2016,
                                        bathrooms=1,
                                        partitioning='Decomandat',
                                        neighborhood='Berceni')
        estate2 = Estate.objects.create(address='strada Voievozilor nr. 15',
                                        price=190128,
                                        rooms=5,
                                        floor=6,
                                        size=150,
                                        year=2015,
                                        bathrooms=1,
                                        partitioning='Decomandat',
                                        neighborhood='Berceni')
        # Listing.objects.create(title='TestListing',
        #                        description='You can see me, but you can\'t buy me, not for sale.',
        #                        user_id=user,
        #                        estate_id=estate)
        for i in range(0, 10):
            Listing.objects.create(title='TestListing',
                                   description='You can see me, but you can\'t buy me, not for sale.',
                                   user_id=user1 if i % 2 == 0 else user2,
                                   estate_id=estate2 if i % 2 == 1 else estate1)

    def test_list_listings_returns_200(self):
        # listings = Listing.objects.all()
        response = self.client.get(reverse('list_listings'))
        self.assertEqual(response.status_code, 200)

    def test_list_listings_returns_correct_template(self):
        response = self.client.get(reverse('list_listings'))
        self.assertTemplateUsed(response, 'list_listings_template.html')

    def test_list_listings_returns_complete_template(self):
        response = response = self.client.get(reverse('list_listings'))

        listings = Listing.objects.all()
        context_listings = response.context['listings']  # page listings

        assert len(listings) == len(context_listings)

        for listing in context_listings:
            assert listing in listings
            # # check listing details
            # self.assertContains(response, listing.title)
            # self.assertContains(response, listing.description)
            # # check year, month and day, not full date
            # self.assertContains(response, listing.updated.year)
            # self.assertContains(response, listing.updated.month)
            # self.assertContains(response, listing.updated.day)
            # # check corresponding estate details
            # self.assertContains(response, listing.estate_id.address)
            # self.assertContains(response, listing.estate_id.price)
            # self.assertContains(response, listing.estate_id.rooms)
            # self.assertContains(response, listing.estate_id.size)
            # self.assertContains(response, listing.estate_id.estimated_price)
            # self.assertContains(response, listing.estate_id.year)
            # self.assertContains(response, listing.estate_id.distance_to_centre)
            # # check corresponding user details
            # self.assertContains(response, listing.user_id.phone_number)
            # self.assertContains(response, listing.user_id.first_name)
