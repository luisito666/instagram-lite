# django Imports
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Modelos
from django.contrib.auth.models import User
from .models import Profile

# Formularios
from .forms import LoginForm

# Exceptions
from django.db.utils import IntegrityError

def auth_view(request):
    if request.user.is_authenticated:
        return redirect('posts:feed')

    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('posts:feed')
            else:
                form = LoginForm()
                return render(request, 'users/login.html', {'message': 'invalid username or password', 'form': form})
        else:
            return render(request, 'users/login.html', {'form': form})

    return render(request, 'users/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error_message': 'Password confirmation does not match'})
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError as e:
            print(e)
            return render(request, 'users/signup.html', {'error_message': 'Username is already in use'})
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        
        return redirect('users:login')

    return render(request, 'users/signup.html')