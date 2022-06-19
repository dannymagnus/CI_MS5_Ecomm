from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Course(models.Model):
    """
    A model class for courses
    """
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    name = models.CharField(
        max_length=(254),
        null=True,
        blank=True,
    )
    friendly_name = models.CharField(
        max_length=(254),
        null=True,
        blank=True,
    )
    description = models.TextField(
        max_length=(1000)
    )
    extra_details = models.TextField(
        max_length=(1000),
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits = 6,
    )
    duration_weeks = models.IntegerField(
    )
    class Level(models.TextChoices):
        """
        A class for choices of dive level
        """
        BEGINNER = "beginner", "Beginner"
        INTERMEDIATE = "intermediate", "Intermediate"
        ADVANCED = "advanced", "Advanced"
        PRO = "4", "professional"

    level = models.CharField(
        max_length=50,
        choices=Level.choices,
        default=Level.BEGINNER
    )
    image = models.ImageField(
        upload_to='courses/',
        blank=True,
        null=True,
        )
    slug = models.SlugField(
        blank=True,
        null=True,
        unique=True,
        )

    def save(self, *args, **kwargs):  # new
        super(Course, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        A method to return the absolute url
        """
        return reverse('course_detail', args=[str(self.slug)])

    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return str(self.name)
