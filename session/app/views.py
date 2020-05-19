from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    request.session['fullname']='NVA'
    return render(request,'index.html')

def page2(request):
    
    return render(request,'page2.html')