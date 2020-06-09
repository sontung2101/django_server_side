from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def createCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    return render(request, 'category_form.html',{'form': form})

@login_required
def updateCategory(request, id):
    category = get_object_or_404(Category, pk=id)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    return render(request, 'category_form.html',{'form': form})

@login_required
def deleteCategory(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('category-list')

@login_required
def listCategory(request):
    categoryList = Category.objects.all()
    return render(request, 'category_list.html', {'categoryList': categoryList})

@login_required
def listProduct(request):
    context = {'products': Product.objects.all()}
    return render(request, 'product_list.html', context)

@login_required
def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    return render(request, 'product_form.html', {'form': form})

@login_required
def updateProduct(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    return render(request, 'product_form.html', {'form': form})

@login_required
def deleteProduct(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('product-list')
