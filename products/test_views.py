# Imports
import tempfile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


# Internal:
from products.models import Category, Product, Brand, Color, Size, Inventory
from products.views import ProductListView, ProductSearchView, product_detail, ProductCreateView 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProductsClassView(TestCase):
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

        test_brand = Brand.objects.create(
            name='test-brand',
        )
        Color.objects.create(
            name = 'test-color',
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
            count=1
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

    def test_list_view_with_one_record(self):
        """
        A test for one product in the products list view
        """
        product = Product.objects.get(name='test-name')

        response = self.client.get(reverse("all_products"))

        self.assertEqual(200, response.status_code)
        self.assertEqual(ProductListView.as_view().__name__, response.resolver_match.func.__name__)

        self.assertTemplateUsed(response, template_name='base.html')
        self.assertTemplateUsed(response, template_name='products/product_list.html')

        context_products = response.context['product_list']
        expected_products = [repr(r) for r in Product.objects.all()]

        self.assertEqual(1, len(context_products))
        self.assertEqual(product, context_products[0])

        self.assertQuerysetEqual(context_products, expected_products, ordered=True)

        self.assertContains(response, product.name)
        self.assertContains(response, product.friendly_name)
        self.assertContains(response, product.price)
        self.assertContains(response, product.brand)
        self.assertNotContains(
            response, '<p class = "fs-6">Sorry no products match your search</p>'
            )

    def test_search_all_products_no_query_string(self):
        """
        This test tests search all products with no query string
        """
        response = self.client.get(reverse('search_products'), {'q': ''})
        self.assertContains(response, '<p class = "fs-6">Sorry no products match your search</p>')

    def test_get_product_detail(self):
        """
        This test tests get product details page and verifies
        """
        product = Product.objects.get(name='test-name')
        response = self.client.get(f'/products/detail/{product.slug}/',
                                   {'product': product})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_add_product_as_superuser(self):
        """
        This test tests add product page as a superuser and verifies
        """
        self.client.login(username='test_super_user', password='test_password')
        response = self.client.get('/products/create_product/')
        self.assertTemplateUsed(response, 'products/create_product.html')

    def test_add_product_as_non_superuser(self):
        """
        This test tests add product page as a non superuser and verifies
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/products/create_product/')
        self.assertEqual(response.status_code, 403)

    def test_add_product_as_superuser_post(self):
        """
        This test tests add product page as a superuser and verifies
        """
        color = Color.objects.get(name='test-color')
        brand = Brand.objects.get(name='test-brand')

        self.client.login(username='test_super_user', password='test_password')
        response = self.client.post('/products/create_product/', {
            'name': 'Test Name 2',
            'price': '99.99',
            'colour': color,
            'brand': brand,
            'description': 'Test Description',
            'image':tempfile.NamedTemporaryFile(suffix=".jpg").name
        })
        self.assertEqual(200, response.status_code)

    def test_get_edit_product_page(self):
        """
        This test tests edit product page(get) as a superuser and verifies
        """
        self.client.login(username='test_super_user', password='test_password')
        product = Product.objects.get(name='test-name')
        response = self.client.get(f'/products/{product.slug}/update/')
        self.assertTemplateUsed(response, 'products/create_product.html')

    def test_edit_product_page_as_non_superuser(self):
        """
        This test tests edit product page as a non superuser and verifies
        """
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/{product.slug}/update/', {
            'name': 'Test Name Update',
            'price': '99.99',
            'colour': 'Test Colour Update',
            'code': '123456',
            'description': 'Test Description Update',
        })
        self.assertEqual(response.status_code, 403)

    def test_delete_product_as_superuser(self):
        """
        This test tests delete product as a superuser and verifies
        """
        self.client.login(username='test_super_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/{product.slug}/delete/')
        self.assertRedirects(response, '/products/')
        deleted_product = Product.objects.filter(id=product.id)
        self.assertEqual(len(deleted_product), 0)

    def test_delete_product_as_non_superuser(self):
        """
        This test tests delete product as a non superuser and verifies
        """
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/{product.slug}/delete/')
        self.assertEqual(response.status_code, 403)

    def test_list_view_with_no_records(self):
        """
        A test for 0 product in the view
        """
        Product.objects.all().delete()

        response = self.client.get(reverse("all_products"))

        self.assertEqual(200, response.status_code)
        self.assertEqual(ProductListView.as_view().__name__, response.resolver_match.func.__name__)

        self.assertTemplateUsed(response, template_name='base.html')
        self.assertTemplateUsed(response, template_name='products/product_list.html')

        self.assertEqual(0, len(response.context["object_list"]))
        self.assertContains(response, '<p class = "fs-6">Sorry no products match your search</p>')
