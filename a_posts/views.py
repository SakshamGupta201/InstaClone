from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views import View
from django.urls import reverse_lazy

# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'a_posts/home.html', context)

class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'a_posts/post_create.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home_view'))
        return render(request, 'a_posts/post_create.html', {'form': form})
