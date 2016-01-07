from django.db import models

class Product(models.Model):
    brand_no = models.CharField(max_length=200)
    brand = models.CharField(max_length=2000)
    product = models.CharField(max_length=2000)
    price_xinglala = models.CharField(max_length=2000)
    xinglala_id = models.CharField(max_length=200)
    images = models.CharField(max_length=2000)

    def __str__(self):
    	return self.product
