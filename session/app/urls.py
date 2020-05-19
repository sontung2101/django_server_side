from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('page2',page2,name='page2'),
    path('accounts/', include('django.contrib.auth.urls')),
]
