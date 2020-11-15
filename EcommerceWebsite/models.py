from django.db import models

# Create your models here.
class Product(models.Model):

    product_name=models.CharField(max_length=500)
    product_category=models.CharField(max_length=200)
    product_description=models.CharField(max_length=5000)
    product_price=models.IntegerField()
    product_image=models.ImageField(upload_to='media',default="")
    
    def __str__(self):
        return self.product_name
