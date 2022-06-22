"""
A module for tests
"""
from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User

# Internal:
from about.models import Faq
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TestContactModels(TestCase):
    """
    A class for testing product models
    """
    def setUp(self):
        """
        Create test user, category, product
        """
        User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@email.com'
        )
        Faq.objects.create(
            name='test_name',
            friendly_name='test_friendly_name',
            question='test_question',
            answer='test_answer'
        )

    def tearDown(self):
        """
        Delete test user, category, product and review
        """
        Faq.objects.all().delete()

    def test_course_str_method(self):
        """
        This test tests the categories str method and verifies
        """
        faq = Faq.objects.get(name='test_name')
        self.assertEqual((faq.__str__()), faq.name)
