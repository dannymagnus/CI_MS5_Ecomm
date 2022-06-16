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
    reason = models.ForeignKey(
        'Reason',
        on_delete=models.CASCADE,
        related_name='reasons'
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


class Reason(models.Model):
    """
    A class for the Reasons model
    """
    reason = models.CharField(
        max_length=100
        )

    def __str__(self):
        """
        Returns the reason name as a string
        """
        return self.reason
