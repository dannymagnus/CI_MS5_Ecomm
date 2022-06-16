"""
A module for models in the products app
"""

import random
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    """
    A class for the category model
    """
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=254
    )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    # Show object by name in admin panel
    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return str(self.name)

    def get_friendly_name(self):
        """
        Returns the category friendly name string
        Args:
            self (object): self.
        Returns:
            The category friendly name string
        """
        return self.friendly_name

class Product(models.Model):
    """
    A class for the product model
    """

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('name',)

    name = models.CharField(
        max_length=254,
        )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
        )

    def get_friendly_name(self):
        """
        Returns the category friendly name string
        Args:
            self (object): self.
        Returns:
            The category friendly name string
        """
        return self.friendly_name

    description = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        )

    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
        )

    brand = models.ForeignKey(
        'Brand',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        )
    holding = models.ManyToManyField(
        'Size',
        through='Inventory',
        max_length=254,
        blank=True,
        )
    color = models.ForeignKey(
        'Color',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        )
    promoted = models.BooleanField(
        default=False,
    )
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        )
    slug = models.SlugField(
        blank=True,
        null=True,
        )

    # Overide save function to create a slug on save -
    # courtesy of Mahmoud Ahmed
    # def save(self, *args, **kwargs):
    #     """
    #     Function to take slug or create on if none exist
    #     """
    #     super(Product, self).save(*args, **kwargs)
    #     if not self.slug and self.name:
    #         self.slug = slugify(self.name)
    #     super(Product, self).save(*args, **kwargs)
    def save(self, *args, **kwargs):  # new
        super(Product, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


    def get_absolute_url(self):
        """
        A method to return the absolute url
        """
        return reverse('product_detail', args=[str(self.slug)])

    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return str(self.name)


class Brand(models.Model):
    """
    A class for product brands
    """
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    name = models.CharField(
        max_length=254
    )

    # Show object by name in admin panel
    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return str(self.name)


class Size(models.Model):
    """
    A class for product sizes
    """
    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    name = models.CharField(
        max_length=254
    )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    def get_friendly_name(self):
        """
        Returns the category friendly name string
        Args:
            self (object): self.
        Returns:
            The category friendly name string
        """
        return self.friendly_name

    # Show object by name in admin panel
    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return str(self.name)


class Color(models.Model):
    """
    A class for the color model
    """
    name = models.CharField(
        max_length=254,
        )

    # Show object by name in admin panel
    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return str(self.name)


class Inventory(models.Model):
    """
    A class for the Inventory model
    """
    class Meta:
        ordering = ('product',)

    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        null=True,
        blank = True,
        )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        blank = True,
        null = True,
        )
    count = models.IntegerField(
        default=0
        )

            #Function to create unique SKU number
    def create_new_sku_number():
        """
        Create new SKU number
        """
        not_unique = True
        while not_unique:
            unique_ref = random.randint(100000, 999999)
            if not Inventory.objects.filter(sku=unique_ref):
                not_unique = False
        return str(unique_ref)

    sku = models.CharField(
        max_length = 10,
        blank=False,
        editable=False,
        unique=True,
        default=create_new_sku_number
        )

    # Show object by name in admin panel
    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return str(self.sku)
