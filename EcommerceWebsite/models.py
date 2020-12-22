from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
   
    product_name=models.CharField(max_length=500)
    product_category=models.CharField(max_length=200)
    product_description=models.CharField(max_length=5000)
    product_price=models.IntegerField()
    product_image=models.ImageField(upload_to='media',default="")
    
    def __str__(self):
        return self.product_name

class ContactUsResponse(models.Model):
    name=models.CharField(max_length=100)
    phoneNumber=models.IntegerField(max_length=13)
    email=models.CharField(max_length=100)
    message=models.CharField(max_length=5000)
    subject=models.CharField(max_length=500)
    def __str__(self):
        return self.name+"_"+self.subject

class CartItem(models.Model):
    customer_id=models.CharField(max_length=100)
    product_id=models.IntegerField()
    product_quantity=models.IntegerField()
    product_add_time=models.DateTimeField(auto_now=True) 
    def __str__(self):
        name=str(self.customer_id)+"_"+str(self.product_id)+"_"+str(self.product_quantity) 
        return name
class CustomerDetail(models.Model):
    customer_id=models.ForeignKey(User, on_delete=models.CASCADE)
    flat_no=models.TextField()
    Street=models.TextField()
    city=models.TextField()
    def __str__(self):
        return self.customer_id.email