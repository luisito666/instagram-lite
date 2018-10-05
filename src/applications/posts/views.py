# import de django
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# importando formularios
from .forms import PostForm

# importando modelos
from .models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
    """
    """
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 10
    context_object_name = 'posts'

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
        return redirect('posts:feed')
    return render(request, 'posts/new.html', {'form': form, 
                                              'user': request.user, 
                                              'profile': request.user.profile })

    