from django.shortcuts import render, HttpResponse,redirect
from .forms import *
from .models import *
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
class OrganisationView(View):
    def get(self,request):
        form = OrganisationForm()
        return render(request, 'org.html',{'form':form})
    def post(self, request):
        form = OrganisationForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Organisation Registered Successfully')
            form.save()
        return render(request,'org.html',{'form':form})



class UserRegistrationView(View):
    def get(self,request):
        form = userregistrationForm()
        return render(request, 'user_register.html',{'form':form})
    def post(self, request):
        form = userregistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('user_pass')
            user.set_password(password)
            user.save()
            messages.success(request, 'Congratulations!! Registered Successfully')
            
        return render(request,'user_register.html',{'form':form})

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        print(username)
        pass1=request.POST.get('pass')
        print(pass1)
        user=authenticate(username=username,password=pass1)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('orga')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render (request,'user_login.html')

