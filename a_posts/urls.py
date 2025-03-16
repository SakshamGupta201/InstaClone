from django.urls import path
from .views import (
    HomeView,
    PostCreateView,
    PostDetailView,
    PostEditView,
    PostDeleteView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home_view"),
    path("create/", PostCreateView.as_view(), name="create_post"),
    path("detail/<uuid:pk>/", PostDetailView.as_view(), name="detail_post"),
    path("edit/<uuid:pk>/", PostEditView.as_view(), name="edit_post"),
    path("delete/<uuid:pk>/", PostDeleteView.as_view(), name="delete_post"),
]
