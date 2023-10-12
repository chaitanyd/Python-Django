from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    # CASCADE - if author deleted then any related book will delete
    # PROTECT - which protect entries related to deleted author
    # SET_NULL - author filed will set to null if related author is deleted
    is_Bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True,
                            blank=True)  # title is harry potter 1 then in url it will harry-potter-1
    published_country = models.ManyToManyField(Country)

    def book_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
