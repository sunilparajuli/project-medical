from django.db import models
from emr.utils.time_stamp_model import TimestampedModel

class Category(TimestampedModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Brand(TimestampedModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Generic(TimestampedModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class ProductCompany(TimestampedModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class ProductUnit(TimestampedModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Product(TimestampedModel):
    name = models.CharField(max_length=120)
    product_code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    generic = models.ForeignKey(Generic, on_delete=models.CASCADE, blank=True, null=True)
    product_company = models.ForeignKey(ProductCompany, on_delete=models.CASCADE, blank=True, null=True)
    product_unit = models.ForeignKey(ProductUnit, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class ProductVariation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute_name = models.CharField(max_length=50)
    attribute_value = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    # Other variation-specific fields

    class Meta:
        unique_together = ['product', 'attribute_name', 'attribute_value']