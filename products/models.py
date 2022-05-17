from django.db import models
import random

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
        return self.name

class Product(models.Model):
    """
    A class for the product model
    """
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    name = models.CharField(
        max_length=254,
        )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
        )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
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
    price = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        )
    rating = models.DecimalField(
        decimal_places=1,
        max_digits=2,
        null=True,
        blank=True,
        )
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        )
    slug = models.SlugField(
        blank=True,
        null=True,
        unique=True,
        )

    # Overide save function to create a slug on save -
    # courtesy of Mahmoud Ahmed
    def save(self, *args, **kwargs):
        """
        Function to take slug or create on if none exist
        """
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    # Show object by name in admin panel
    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return self.name


class Brand(models.Model):
    
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
        return self.name


class Size(models.Model):
    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

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
        return self.name


class Color(models.Model):
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
        return self.name


class Inventory(models.Model):
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE
        )
    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
        )
    count = models.IntegerField(
        default=0
        )
    
            #Function to create unique SKU number
    def create_new_sku_number():
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
        return self.sku
