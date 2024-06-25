from .models import Records
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
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
        return redirect('home')

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

    context = {
        'form': form
    }
    
    return render(request, 'sign-in.html', context)