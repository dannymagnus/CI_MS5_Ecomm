from django.contrib.auth.models import User
from django.test import TestCase

# Internal:
from courses.models import Course
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProductModels(TestCase):
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
        Course.objects.create(
            name='test-course',
            friendly_name='Test Course',
            price='1000',
            duration_weeks='1'
        )


    def tearDown(self):
        """
        Delete test user, category, product and review
        """
        User.objects.all().delete()
        Course.objects.all().delete()

    def test_course_str_method(self):
        """
        This test tests the categories str method and verifies
        """
        course = Course.objects.get(name='test-course')
        self.assertEqual((course.__str__()), course.name)
