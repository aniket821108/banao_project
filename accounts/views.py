from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import CustomUserCreationForm, AddressForm
from .models import CustomUser
from django.contrib.auth import logout as auth_logout 

def home(request):
    return render(request, 'accounts/home.html')

def aboutUS(request):
    return render(request, 'accounts/aboutUs.html')

def signup(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, request.FILES)
        address_form = AddressForm(request.POST)
        
        if user_form.is_valid() and address_form.is_valid():
            address = address_form.save()
            user = user_form.save(commit=False)
            user.address = address
            user.save()
            
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            
            if user.user_type == 'P':
                return redirect('patient_dashboard')
            else:
                return redirect('doctor_dashboard')
    else:
        user_form = CustomUserCreationForm()
        address_form = AddressForm()
    
    return render(request, 'accounts/signup.html', {
        'user_form': user_form,
        'address_form': address_form
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            if user.user_type == 'P':
                return redirect('patient_dashboard')
            else:
                return redirect('doctor_dashboard')
    
    return render(request, 'accounts/login.html')

def user_logout(request):
    auth_logout(request)
    return redirect('home')

def patient_dashboard(request):
    if not request.user.is_authenticated or request.user.user_type != 'P':
        return redirect('login')
    return render(request, 'accounts/patient_dashboard.html', {'user': request.user})

def doctor_dashboard(request):
    if not request.user.is_authenticated or request.user.user_type != 'D':
        return redirect('login')
    return render(request, 'accounts/doctor_dashboard.html', {'user': request.user})