from django.contrib import admin
from .models import Product,ContactUsResponse, CartItem, CustomerDetail
# Register your models here.

admin.site.register(Product)
admin.site.register(ContactUsResponse)
admin.site.register(CartItem)
admin.site.register(CustomerDetail)
