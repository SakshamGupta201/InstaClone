from django.shortcuts import render
from .models import Post
from .forms import PostCreateForm, PostEditForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "a_posts/home.html"
    context_object_name = "posts"


class PostCreateView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "a_posts/post_create.html"
    success_url = reverse_lazy("home_view")
    success_message = "Post created successfully"


class PostDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = "a_posts/post_delete.html"
    success_url = reverse_lazy("home_view")
    context_object_name = "post"
    success_message = "Post deleted successfully"


class PostEditView(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = "a_posts/post_edit.html"
    context_object_name = "post"
    success_url = reverse_lazy("home_view")
    success_message = "Post updated successfully"

class PostDetailView(DetailView):
    model = Post
    template_name = "a_posts/post_detail.html"
    context_object_name = "post"


def custom_404_view(request, exception):
    return render(request, "404.html", {}, status=404)
