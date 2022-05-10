from django.db import models

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
    size = models.CharField(
        max_length=254,
        null=True,
        blank=True
        )
    color = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        )
    rating = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        null=True,
        blank=True,
        )
    sku = models.IntegerField(
        )
    image_url = models.URLField(
        )
    image = models.ImageField(
        upload_to='meals/',
        blank=True
        )
    slug = models.SlugField(
        blank=True,
        null=True
        )

    # Overide save function to create a slug on save -
    # courtesy of Mahmoud Ahmed
    def save(self, *args, **kwargs):
        """
        Function to take slug or create on if none exist
        """
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meal, self).save(*args, **kwargs)

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
