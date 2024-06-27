from .models import Records
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, LoginForm, AddRecordForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'index.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('user_login')
        

    context = {
        'form': form
    }

    return render(request, 'register.html', context=context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')

    context = {
        'form': form
    }
    
    return render(request, 'user_login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login_user')


@login_required(login_url='login_user')
def dashboard(request):
    user_records = Records.objects.all()
    context = {
        'records': user_records
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='login_user')
def create_record(request):
    form = AddRecordForm()

    if request.method == 'POST':
        form = AddRecordForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = {
        'form': form
    }

    return render(request, 'create_record.html', context)