from django.urls import path, include
from .views_admin import *
from .views_accounts import *
from .views_user import *

urlpatterns = [
  #User pages
  path('',index,name='home'),
  path('view_product/<int:id>',viewProduct,name='product-view'),
  path('purchase/<int:id>',purchase,name='purchase'),
  path('purchase_confirm/<int:id>',purchaseConfirm,name='purchase-confirm'),
  path('thank_you/<int:id>',thankYou,name='thank-you'),

  #Accounts
  path('accounts/', include('django.contrib.auth.urls')),                 # new
  path('accounts/signup', signup, name='signup'),   

  #Admin pages
  
  path('create_category', createCategory, name='category-create'),
  path('update_category/<int:id>', updateCategory, name='category-update'),
  path('delete_category/<int:id>', deleteCategory, name='category-delete'),
  path('list_category', listCategory, name='category-list'),

  path('staff', listProduct, name='product-list'),
  path('create_product', createProduct, name='product-create'),
  path('update_product/<int:id>',updateProduct, name='product-update'),
  path('delete_product/<int:id>',deleteProduct, name='product-delete'),
]

