from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
#utilities
def slideCounter(l):
    slides=0
    while(l>0):
        if(l>=4):
            slides=slides+1
            l=l-4
        elif(l<4 and l>0):
            slides=slides+1
            l=l-l
    return slides
# Create your views here.
def ecommHome(request):
    product_data={}
    product=Product.objects.all()
    category_dict={}
    category_list=[]
    for p in product:
        category_dict[p.product_category]=" "
    for k,v in category_dict.items():
        category_list=[]
        cat_slide=0
        dict_list=[]
        for p in product:
            if k==p.product_category:
                category_list.append(p)
        dict_list.append(category_list)
        dict_list.append(range(0,slideCounter(len(category_list))))
        category_dict[k]=dict_list
              

    #slides=0
   # l=len(product)
    #slides=self.slideCounter(l)
    #product_data['slides']=slides
    #product_data['product']=product
    #product_data['prange']=range(1,slides)
    
    return render(request,'ecommHome.html', {'all_prod':category_dict.items()})

def ecommCart(request):
    return HttpResponse("Cart")

def ecommAboutUs(request):
    return HttpResponse("About US")

def ecommContactUs(request):
    return HttpResponse("Contact Us")

def ecommProductPage(request):
    return HttpResponse("Product Page")