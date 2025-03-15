from django.shortcuts import render

# Create your views here.
def home_view(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title": title,
    }
    return render(request, 'a_posts/home.html', context)