# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from django.test import TestCase

# Internal:
from products.models import Category, Product, Inventory, Brand, Color
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProductModels(TestCase):
    """
    A class for testing product models
    """
    def setUp(self):
        """
        Create test user, category, product
        """
        # test_user = User.objects.create_user(
        #     username='test_user', 
        #     password='test_password'
        #     )
        
        brand = Brand.objects.create(
            name = 'test_brand',
            )

        category = Category.objects.create(
            name='test_category', 
            friendly_name='test_category',
            )
        
        color = Color.objects.create(
            name = 'Test_Color',
        )

        product = Product.objects.create(
            name='my product',
            friendly_name='my product',
            holding=size,
            price='399.00',
            
        )
        
        # inventory = Inventory.objects.create(
        #     sku = '565456'
        # )
        
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
        category = Category.objects.get(name='test_category')
        self.assertEqual((category.__str__()), category.name)
        self.assertEqual(category.get_friendly_name(), category.friendly_name)

    # def test_product_str_method(self):
    #     """
    #     This test tests the products str method and verifies
    #     """
    #     product = Product.objects.get(name='my-product')
    #     self.assertEqual((product.__str__()), product.name)
    #     self.assertEqual(product.get_friendly_name(), product.friendly_name)

    def test_brand_str_method(self):
        """
        This test tests the reviews str method and verifies
        """
        review = Brand.objects.get(name='test_brand')
        self.assertEqual((brand.__str__()), brand.name)

