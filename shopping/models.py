from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator
# Create your models here.


class Product(models.Model):
	name = models.CharField(max_length=128)
	price = models.DecimalField(default=0,decimal_places=2, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
	quantity = models.CharField(max_length=128)
	image = models.FileField()
	status = models.BooleanField(default=True)

	def __str__(self):
		return self.name