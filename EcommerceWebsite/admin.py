from django.contrib import admin
from .models import Product,ContactUsResponse, cartItem
# Register your models here.

admin.site.register(Product)
admin.site.register(ContactUsResponse)
admin.site.register(cartItem)