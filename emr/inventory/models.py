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


""" ## todo => product has variation, variation has batches, each batches might have different prices
class VariationBatch(models.Model):
	fk_variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE,)
	# fk_purchaseitem = models.ForeignKey("orders.PurchaseItem", on_delete=models.CASCADE, null=True)
	quantity = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
	batchno = models.CharField(max_length=100, null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=20)
	sale_price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
	created_at = models.DateField(default=date.today)
	expiry_date = models.DateField(null=True, blank=True)
	purchase_date = models.DateField(null=True, blank=True)
	use_batch = models.BooleanField(default=True)
	is_initial = models.BooleanField(default=False, blank=True)

	def __str__(self):
		return '%s-%s' %(self.fk_variation.title, self.batchno)




class VariationPrice(models.Model):
	user_type = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #for patient type drug filter
	fk_variation = models.ForeignKey(Variation, on_delete=models.CASCADE, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=20, null=True)
	sale_price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)

class VariationBatchPrice(models.Model):
	fk_user_type = models.ForeignKey(UserTypes, on_delete=models.CASCADE, null=True) #for patient type drug filter
	fk_variation_batch = models.ForeignKey(VariationBatch, on_delete=models.CASCADE, null=True) #for patient type drug filter
	price = models.DecimalField(decimal_places=2, max_digits=20, null=True)
	sale_price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)

	def __str__(self):
		return 'batch number :%s for Patient-type-[%s]-price-%s' %(self.fk_variation_batch.batchno, self.fk_user_type.title, self.price)
"""