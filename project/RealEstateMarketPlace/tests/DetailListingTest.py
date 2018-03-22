from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from ..models import Listing, User, Estate

class DetailListingTest(TestCase):
	def setUp(self):
		user = 	User.objects.create(email="admin@maildrop.cc",password="admin123",
			first_name="Mihai",last_name="Ghidoveanu",phone_number="0728622410")
		estate = Estate.objects.create(city="Bucuresti")
		Listing(title="TestListing",description="This is the listing",user_id=user,estate_id=estate,
			phone_number="0728421123").save()


	def test_detail_listing_returns_a_listing(self):
		listing = Listing.objects.all()[0]
		response = self.client.get(reverse('details_listing',args = (listing.id,)))
		self.assertEqual(response.status_code,200)

	def test_detail_listing_returns_correct_template(self):
		listing = Listing.objects.all()[0]
		response = self.client.get(reverse('details_listing',args = (listing.id,)))
		self.assertTemplateUsed(response,'detail_listing_template.html')

	def test_detail_listing_returns_complete_template(self):
		listing = Listing.objects.all()[0]
		response = self.client.get(reverse('details_listing',args = (listing.id,)))
		# check listing details
		self.assertContains(response,listing.title)
		self.assertContains(response,listing.description)
		# check year, month and day, not full date
		self.assertContains(response,listing.updated.year)
		self.assertContains(response,listing.updated.month)
		self.assertContains(response,listing.updated.day)
		# check corresponding estate details
		self.assertContains(response,listing.estate_id.city)
		self.assertContains(response,listing.estate_id.address)
		self.assertContains(response,listing.estate_id.price)
		self.assertContains(response,listing.estate_id.rooms)
		self.assertContains(response,listing.estate_id.size)
		self.assertContains(response,listing.estate_id.estimated_price)
		self.assertContains(response,listing.estate_id.year)
		self.assertContains(response,listing.estate_id.distance_to_centre)
		# check corresponding user details
		self.assertContains(response,listing.user_id.email)
		self.assertContains(response,listing.user_id.phone_number)
		self.assertContains(response,listing.user_id.first_name)
		self.assertContains(response,listing.user_id.last_name)

	def test_detail_listing_template_contains_delete_button(self):
		pass

	def test_detail_listing_template_contains_favorite_button(self):
		pass
