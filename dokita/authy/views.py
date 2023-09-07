from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from verify_email.email_handler import send_verification_email

from django.contrib import messages, auth
from .models import User
from.forms import MyUserCreationForm

# Create your views here.

def user_register(request):
    page = 'register'      
    form = MyUserCreationForm()
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
                    inactive_user = send_verification_email(request, form)
                    inactive_user.username = inactive_user.username.upper()
                    inactive_user.email = inactive_user.email.lower()
                    messages.success(request, f'Account created for {inactive_user.username} successfully!. Kindly check you email "<strong> {inactive_user.email} </strong>" to activate your account')
                    # return redirect('settings', pk=user.username)
                    return redirect('home')

        else:
            messages.error(request, 'Passwords Does Not Match')
            return redirect('register')
            
    
    context={'form': form, 'page': page}
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

class ResetPasswordView(PasswordResetView, SuccessMessageMixin):
    template_name = 'authy/password_reset.html'
    email_template_name = 'authy/password_reset_email.html'
    subject_template_name = 'authy/password_reset_subject.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')