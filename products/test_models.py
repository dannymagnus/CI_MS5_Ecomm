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
        test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@email.com'
        )
        test_category = Category.objects.create(
            name='test-category',
            friendly_name='Test Category'
        )
        test_brand = Brand.objects.create(
            name='test-brand',
        )
        test_color = Color.objects.create(
            name = 'test-color',
        )
        product = Product.objects.create(
            name='test-name',
            friendly_name='Test Name',
            price=100,
            brand=test_brand,
            description='Test Description',
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

    def test_category_str_method(self):
        """
        This test tests the categories str method and verifies
        """
        category = Category.objects.get(name='test-category')
        self.assertEqual((category.__str__()), category.name)
        self.assertEqual(category.get_friendly_name(), category.friendly_name)

    def test_brand_str_method(self):
        """
        This test tests the categories str method and verifies
        """
        brand = Brand.objects.get(name='test-brand')
        self.assertEqual((brand.__str__()), brand.name)

    def test_color_str_method(self):
        """
        This test tests the categories str method and verifies
        """
        color = Color.objects.get(name='test-color')
        self.assertEqual((color.__str__()), color.name)

    def test_product_str_method(self):
        """
        This test tests the categories str method and verifies
        """
        product = Product.objects.get(name='test-name')
        self.assertEqual((product.__str__()), product.name)

    def test_product_save_method(self):
        """
        This test tests the categories str method and verifies
        """
        product = Product.objects.get(name='test-name')
        self.assertEqual(product.slug, 'test-name')

    def test_get_absolute_url(self):
        """
        This test tests the product get absolute url method and verifies
        """
        product = Product.objects.get(name='test-name')
        self.assertEqual("/products/detail/test-name/", product.get_absolute_url())

    def test_get_friendly_name(self):
        """
        This test tests the product get friendly name method and verifies
        """
        product = Product.objects.get(name='test-name')
        self.assertEqual(product.get_friendly_name(), 'Test Name')
