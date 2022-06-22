"""
A module for tests
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
import tempfile
from django.contrib.messages import get_messages
from django.test import TestCase

# Internal:
from products.models import Inventory, Product, Brand, Size
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TestBagViews(TestCase):
    """
    A class for testing bag views
    """

    def setUp(self):
        test_brand = Brand.objects.create(
            name='test-brand',
        )
        size = Size.objects.create(
            name = 'test-size',
        )
        product = Product.objects.create(
            name='test-name',
            friendly_name='Test Name',
            price=100,
            brand=test_brand,
            description='Test Description',
            image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        Inventory.objects.create(
            product=product,
            size=size,
            count=1,
            sku = '777777'
        )

    def test_get_bag_page(self):
        """
        This test checks that the bag page is displayed
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_empty_bag_no_size(self):
        """
        This test adds a product to an empty bag and verifies
        """
        product = Product.objects.get(name='test-name')
        Inventory.objects.get(sku='777777')
        response = self.client.post(f'/bag/{product.slug}/add/',
                                    {"quantity": 1, 'sku': '777777', "redirect_url": "view_bag"})
        bag = self.client.session['bag']
        self.assertEqual(list(bag.keys())[0], '777777')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Added Test Name to your bag')
