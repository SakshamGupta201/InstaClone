from django.urls import path    
from . import views

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("create/", views.PostCreateView.as_view(), name="create_post"),
    path("delete/<uuid:pk>/", views.post_delete_view, name="delete_post"),
]
