
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Faq(models.Model):
    """
    A model class to record and present faqs
    """
    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    name = models.CharField(
        max_length=254
        )
    friendly_name = models.CharField(
        max_length=254,
        )
    question = models.TextField(
        max_length=1000,
        )
    answer = models.TextField(
        max_length=1000,
        )

    def __str__(self):
        return self.name
