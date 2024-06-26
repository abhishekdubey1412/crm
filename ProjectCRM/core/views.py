from .models import Records
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, LoginForm

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
            return redirect('sign_in')
        

    context = {
        'form': form
    }

    return render(request, 'register.html', context=context)


def sign_in(request):
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
    
    return render(request, 'sign-in.html', context)


def sign_out(request):
    logout(request)
    return redirect('sign_in')


@login_required(login_url='sign_in')
def dashboard(request):
    user_records = Records.objects.all()
    context = {
        'records': user_records
    }
    return render(request, 'dashboard.html', context)