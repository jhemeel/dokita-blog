from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from django.contrib import messages, auth
from .models import User
from.forms import MyUserCreationForm

# Create your views here.


def user_regsiter(request):
    
    page = 'register'
    form = MyUserCreationForm
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'Email aleady Exists')
                              
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.warning(request, 'User aleady Exists')
                return redirect('register')
                
            else:
                form = MyUserCreationForm(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    # user.username = user.username.capitalize()
                    user.save()
                    messages.success(request, f"Account created for {user.username} successfully!")
                    return redirect('login')
    context={'page': page, 'form': form}
    return render(request, 'authy/login_register.html', context)


def user_login(request):
      
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        
        user = authenticate(email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'{user.username} is successfully logged In!')  
            return redirect('home')          
            # return redirect('profile', pk=user.username)
        
        else:
            messages.info(request, 'Credentials Invalid!, Please enter the correct email and password. Note that both fields may be case-sensitive.')
            return redirect('login')
        
    context = {}
    return render(request, 'authy/login_register.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')