from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

# Create your views here.

@login_required
def list_post(request):
    """
    """
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts,
                                               'user': request.user})

@login_required
def create_post(request):
    """
    """
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('feed')
    return render(request, 'posts/new.html', {'form': form, 
                                              'user': request.user, 
                                              'profile': request.user.profile })

    