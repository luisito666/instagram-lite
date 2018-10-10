# import de django
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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


class PostsDetailView(LoginRequiredMixin, DetailView):
    """
    """
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """
    """
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_contex_data(self, **kwargs):
        """
        """
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        # context['profile'] = self.request.user.profile
        return context
   

"""
@login_required
def list_post(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts,
                                               'user': request.user})

@login_required
def create_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('posts:feed')
    return render(request, 'posts/new.html', {'form': form, 
                                              'user': request.user, 
                                              'profile': request.user.profile })
"""
