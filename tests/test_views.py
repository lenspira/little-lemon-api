from django.test import TestCase, RequestFactory
from restaurant.models import Menu, Booking
from restaurant.views import MenuItemsView

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Ice Cream", price=7, inventory=100)
        Menu.objects.create(title="Bruschetta", price=14, inventory=50)
        Menu.objects.create(title="Grilled Fish", price=21, inventory=25)
        return super().setUp()

    def test_getall(self):
        request = RequestFactory().get('/restaurant/menu/')
        view = MenuItemsView()
        view.setup(request)
        context = str(view.get_queryset())
        self.assertIn('Ice Cream : 7.00', context)
        self.assertIn('Bruschetta : 14.00', context)
        self.assertIn('Grilled Fish : 21.00', context)