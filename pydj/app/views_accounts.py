from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
   form = UserCreationForm()
   
   if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username,
                                    password=request.POST['password1'])
            login(request, user)
            return redirect('product-list')

   return render(request, 'registration/signup.html', { 'form':  form})
