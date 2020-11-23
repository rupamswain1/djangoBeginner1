from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, ContactUsResponse, CartItem

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

def ecommCart(request,product_id, operation):
    if operation=='addToCart':
        product=Product.objects.get(id=product_id)
        cart=CartItem.objects.filter(product_id=product_id)
        if(len(cart)==0):
             cart =CartItem(customer_id=1234, product_id=product.id, product_quantity=1)
        else:
            cart=CartItem.objects.get(product_id=product_id)
            cart.product_quantity=cart.product_quantity+1
        cart.save()
        cart=CartItem.objects.filter(customer_id=1234).order_by('-product_add_time')
        
        cartItem=[]
        tempList={}
        for obj in cart:
            id=obj.product_id
            #print(id)
            tempList={}
            prod=Product.objects.filter(id=id)
            tempList['product_data']=prod[0]
            tempList['product_quantity']=obj.product_quantity
            tempList['product_add_time']=obj.product_add_time
            cartItem.append(tempList)
            
       
    return render(request,'cart.html',{'cartItem':cartItem})

def ecommAboutUs(request):
    return render(request,'aboutUs.html')

def ecommContactUs(request):
    if request.method=='GET':
        return render(request,'contactUs.html')
    else:
        name=request.POST.get('name')
        phoneNumber=request.POST.get('phoneNumber',None)
        email=request.POST.get('email',None)
        message=request.POST.get('message', None)
        subject=request.POST.get('subject',None)
        flag=False
        if(name!=None and phoneNumber!=None and email!=None and message!=None and subject!=None):
            contactUs=ContactUsResponse(name=name, phoneNumber=phoneNumber,email=email,message=message,subject=subject)
            contactUs.save()
            flag=True
        return render(request,'contactUs.html',{'saved':flag,'name':name})
def ecommProductPage(request,product_id):
    product=Product.objects.get(id=product_id)

    return render(request,'productPage.html',{'product':product})