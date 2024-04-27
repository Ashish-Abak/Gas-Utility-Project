from django.shortcuts import render,redirect
from gas_app.forms import ServiceRequestForm
from gas_app.models import ServiceRequest
from django.contrib.auth import authenticate,login,logout
from gas_app.forms import LoginForm,SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass= form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url=login)
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST,request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

def request_tracking(request):
    service_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'request_tracking.html', {'service_requests': service_requests})
