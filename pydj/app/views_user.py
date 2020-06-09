from django.shortcuts import HttpResponse,render,get_object_or_404,redirect
from .models import *
from .forms import *

def index(request):
    productList = Product.objects.all()
    categoryList = Category.objects.all()
    queryParams = request.GET


    prodcuctName = queryParams.get('product_name')
    categoryId = queryParams.get('category_id')
    priceRange = queryParams.get('price_range')
    minPrice,maxPrice =None,None
    priceTable ={
        '1':[None,10],
        '2':[10,15],
        '3':[15,20],
        '4':[20,None]
    }
    if priceRange:
        minPrice,maxPrice = priceTable.get(priceRange)
    if prodcuctName:
        productList = productList.filter(name__contains=prodcuctName)
    
    if categoryId:
        productList = productList.filter(category__id = int(categoryId))
    
    if minPrice:
        productList = productList.filter(price__gte = minPrice*1e6) #lớn hơn hoặc bằng
    if maxPrice:
        productList = productList.filter(price__lte = maxPrice*1e6) #nhỏ hơn hoặc bằng
    return render(request,'user/index.html',{'productList':productList,'categoryList':categoryList,'queryParams':queryParams})


def viewProduct(request,id):
    product = get_object_or_404(Product,id =id)
    return render(request,'user/view_product.html',{'product':product})

def purchase(request,id):
    product = get_object_or_404(Product,id =id)
    form = ContactForm()
    if  request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            request.session['form']=form.cleaned_data
            return redirect('purchase-confirm', id)
    return render(request,'user/purchase.html',{'product':product,'form':form})

def purchaseConfirm(request,id):
    product = get_object_or_404(Product,pk = id)
    form = request.session.get('form')
    return render(request,'user/purchase_confirm.html',{'product':product,'form':form})

def thankYou(request,id):
    product = get_object_or_404(Product,pk = id)
    form = request.session.get('form')
    return render(request,'user/thank_you.html',{'product':product,'form':form})