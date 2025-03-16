from django.shortcuts import render, redirect
from .models import Post
from .forms import PostCreateForm, PostEditForm
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DeleteView, UpdateView


# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "a_posts/home.html"
    context_object_name = "posts"


class PostCreateView(View):
    def get(self, request):
        form = PostCreateForm()
        return render(request, "a_posts/post_create.html", {"form": form})

    def post(self, request):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Post created successfully")
            return redirect(reverse_lazy("home_view"))
        return render(request, "a_posts/post_create.html", {"form": form})


class PostDeleteView(DeleteView):
    model = Post
    template_name = "a_posts/post_delete.html"
    success_url = reverse_lazy("home_view")
    context_object_name = "post"

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Post deleted successfully")
        return super().delete(request, *args, **kwargs)


class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = "a_posts/post_edit.html"
    context_object_name = "post"
    success_url = reverse_lazy("home_view")

    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully")
        return super().form_valid(form)


class PostDetailView(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, "a_posts/post_detail.html", {"post": post})
