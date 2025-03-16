from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "a_posts/home.html", context)


class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, "a_posts/post_create.html", {"form": form})


def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect(reverse_lazy("home_view"))
    context = {"post": post}
    return render(request, "a_posts/post_delete.html", context)
