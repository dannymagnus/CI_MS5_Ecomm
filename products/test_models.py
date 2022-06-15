"""
A test module for models in the products app
"""# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from django.test import TestCase

# Internal:
from products.models import Category, Product, Inventory, Brand, Color, Size
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProductModels(TestCase):
    """
    A class for testing product models
    """
    def setUp(self):
        """
        Create test user, category, product
        """
        brand=Brand.objects.create(
            name = 'test_brand',
            )
        color=Color.objects.create(
            name='test_color',
        )
        size=Size.objects.create(
                name='test_size',
        )
        tag1 =Inventory.objects.create(
            sku='454664',
            size=size,
            count=0,
        )
        tag2=Inventory.objects.create(
            sku='454889',
            size=size,
            count=0,
        )
        Product.objects.create(
            name = 'test_product',
            brand=brand,
            color=color,
            price='399.00',
        )


    def tearDown(self):
        """
        Delete test user, category, product and review
        """
        User.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()
        Brand.objects.all().delete()
        Color.objects.all().delete()
        Inventory.objects.all().delete()

    def test_product_str_method(self):
        """
        This test tests the products str method and verifies
        """
        product = Product.objects.get(name='test_product')
        self.assertEqual((product.__str__()), product.name)