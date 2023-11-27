from django.db import models
from emr.utils.time_stamp_model import TimestampedModel
# Create your models here.
from emr.patients.models import Patient
from django.db.models.signals import post_save
from django.dispatch import receiver
from emr.inventory.models import Product
class Bill(TimestampedModel):
    customer = models.ForeignKey(Patient, on_delete=models.CASCADE, )
    bill_number = models.CharField(max_length=20, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customer.first_name}"

@receiver(post_save, sender=Bill)
def update_bill_number(sender, instance, created, **kwargs):
    if created and not instance.bill_number:
        instance.bill_number = f"MED{instance.pk}"
        instance.save()

class BillItem(TimestampedModel):
	bill = models.ForeignKey(Bill, on_delete=models.SET_NULL, null=True, blank=True)
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	price = models.DecimalField(max_digits=5, decimal_places=2)
	ordered_price = models.DecimalField(max_digits=5, decimal_places=2)
	amount = models.DecimalField(max_digits=8, decimal_places=2)

@receiver(post_save, sender=BillItem)
def update_amount(sender, instance, created, **kwargs):
    if created or instance.quantity != instance._original_quantity or instance.price != instance._original_price:
        # Calculate the new amount
        instance.amount = instance.quantity * instance.price
        instance.save(update_fields=['amount'])