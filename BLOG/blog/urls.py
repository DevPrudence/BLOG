from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from . import views


urlpatterns = [
    path("register", views.register_request, name="register"),
    path ('post/<int:pk>/edit/', BlogDeleteView.as_view(), name = 'post_delete'),
    path ('post/<int:pk>/edit/', BlogUpdateView.as_view(), name = 'post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path ('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),
    path ('', BlogListView.as_view(), name = 'home'),
]
