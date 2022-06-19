# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

# Internal:
from products.models import Category, Product, Brand, Color, Size, Inventory
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProductViews(TestCase):
    """
    A class for testing product views
    """
    def setUp(self):
        """
        Create test user(regular and super user), category and product
         """
        User.objects.create_user(
            username='test_user', password='test_password')

        User.objects.create_superuser(
            username='test_super_user', password='test_password')

        Category.objects.create(
            name='test-category', friendly_name='test category')

        color = Color.objects.create(
            name='test-color',
        )

        Product.objects.create(
            name='Test Name',
            price='99.99',
            color=color,
            description='Test Description',
        )

    def tearDown(self):
        """
        Delete test user, category, product
        """
        User.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()
        Brand.objects.all().delete()
        Color.objects.all().delete()
        Size.objects.all().delete()
        Inventory.objects.all().delete()

    def test_get_all_products(self):
        """
        This test tests get all products page and verifies
        """
        response = self.client.get('/products/', {'search_term': 'test',
                                                  'current_categories': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
