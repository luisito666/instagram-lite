# django Imports
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy

# Modelos
from django.contrib.auth.models import User
from .models import Profile
from applications.posts.models import Post

# Formularios
from .forms import LoginForm, SignupForm

# Exceptions
from django.db.utils import IntegrityError
from django.contrib.auth import views as auth_views

from platzigram import settings


class SignupView(FormView):
    """
    """
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """
        """
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    """
    """
    template_name = 'users/login.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().get(*args, **kwargs)


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """
    """
    # template_name = 'users/logout.html'


class UserDetailView(LoginRequiredMixin, DetailView):
    """
    """
    queryset = User.objects.all()
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name='users/detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """
    """
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """
        """
        return self.request.user.profile

    def get_success_url(self):
        """
        """
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


"""
def auth_view(request):
    if request.user.is_authenticated:
        return redirect('posts:feed')

    form = LoginForm(request.POST or None)
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
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('users:login')

    return render(request, 'users/signup.html', {'form': form})

def signup_view_old(request):
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

@login_required
def update_profile(request):
    form = ProfileForm(request.POST or None, request.FILES or None)
    profile = request.user.profile

    if form.is_valid():
        profile.website = form.cleaned_data['website']
        profile.phone_number = form.cleaned_data['phone_number']
        profile.biography = form.cleaned_data['biography']
        profile.picture = form.cleaned_data['picture']
        profile.save()
        
        url = reverse('users:detail', kwargs={'username': request.user.username})
        return redirect(url)

    context = {
        'profile': profile,
        'user': request.user,
        'form': form
    }
    return render(request, 'users/update_profile.html', context)
"""