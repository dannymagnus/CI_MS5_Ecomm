# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Contact(models.Model):
    """
    A class for the contact model
    """
    class Reason(models.TextChoices):
        """
        A subclass for reasons choices
        """
        SHOP = "1", "Dive Equipment Shop / Online Orders"
        COURSE = "2", "Diving Courses"
        GENERAL = "3", "General Enquiry"
        # (...)

    reason = models.CharField(
        max_length=2,
        choices=Reason.choices,
        default=Reason.SHOP
    )
    name = models.CharField(
        max_length=50
        )
    email = models.EmailField(
        max_length=70
        )
    phone = models.CharField(
        max_length=13
        )
    postcode = models.CharField(
        max_length=10
        )
    street_address = models.CharField(
        max_length=100
        )
    message = models.TextField(
        max_length=300
        )
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        """
        Returns the contact name as a string
        """
        return self.name
