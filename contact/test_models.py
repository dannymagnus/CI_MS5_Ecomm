"""
A module for model tests
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django.test import TestCase
from django.contrib.auth.models import User
# Internal:
from contact.models import Contact
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
        Contact.objects.create(
            reason='test_reason',
            name='test_name',
            email='test@email,.com',
            phone='test_phone',
            postcode='test_postcode',
            street_address='test_address',
            message='test_message'
        )

    def tearDown(self):
        """
        Delete test user, category, product and review
        """
        Contact.objects.all().delete()

    def test_course_str_method(self):
        """
        This test tests the categories str method and verifies
        """
        contact = Contact.objects.get(name='test_name')
        self.assertEqual((contact.__str__()), contact.name)
