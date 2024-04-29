from django.shortcuts import render,redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib import auth
# Create your views here.



class UsernameValidationView(View):
    def get(self,request):
        data =json.loads(request.body)
        username=data['username']
        if not str(username).isalnum():
            return JsonResponse({'username error':'username should only contain alphanumeric characters'},status=400)
        return JsonResponse({'username_valid':True})
    
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username error':'sorry username in use, choose another one'},status=409)
        return JsonResponse({'username_valid':True})
    

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists!')
            return render(request, 'authentication/register.html')
        else:
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'email already exists!')
                return render(request, 'authentication/register.html')
            else:           
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                messages.success(request, 'successfully registered.')
                return render(request, 'authentication/register.html')
        

class LoginView(View):
    def get(self,request):
        return render(request, 'authentication/login.html')
    
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username and password:
            user=auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'welcome, '+ user.username+' You are now logged in')
                    return redirect('expenses')
            else:
                messages.error(request, 'Invalid Credentials,please try again')
            return render(request, 'authentication/login.html')
        
class LogoutView(View):
    def post(self,request):
        auth.logout(request)
        messages.success(request,'You have been logged out')
        return redirect('login')
            