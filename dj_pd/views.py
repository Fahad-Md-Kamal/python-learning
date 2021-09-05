from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def home_view(request):
    return render(request, 'home.html', {})


def login_view(request):
    error_message = None
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = authenticate(username, password=password)
            if user is not None:
                login(request, user)
            else:
                error_message = "Oops..!! Something went wrong..."

    context = {
        'form': form
    }
    return render(request, 'login.html', context)
