from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice Cream", price=80, inventory=100)
        self.assertEqual(str(item), 'Ice Cream : 80')

class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="Jack Brown", no_of_guests=2, booking_date="2024-06-15")
        self.assertEqual(str(item), 'Jack Brown for 2 on 2024-06-15')