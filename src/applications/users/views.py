from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

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
    return render(request, 'users/signup.html')