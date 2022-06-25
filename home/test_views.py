"""
A module for tests
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase

# Internal:

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestIndexViews(TestCase):
    """
    Test the index view page
    """
    def test_index_page(self):
        """
        Test the index view
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_404_error_page(self):
        """
        Test the 404 error page, when incorrect url is entered
        """
        response = self.client.get('/df')
        self.assertEqual(response.status_code, 404)
