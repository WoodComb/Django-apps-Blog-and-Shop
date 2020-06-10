from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView)
from . import views
urlpatterns = [
    path('', PostListView.as_view(), name = "home-page"),
    path('post/<int:pk>/', PostDetailView.as_view(), name = "detail-page"),
    path('post/new/', PostCreateView.as_view(), name = "create-page"),
    path('profile/', views.user, name = "user-page"),
    path('register/', views.register, name="register-page"),
    path('login/', auth_views.LoginView.as_view(template_name='userpost/login.html'), name="login-page"),
    path('logout/', auth_views.LogoutView.as_view(template_name='userpost/logout.html'), name="logout-page"),
    path('profile/', views.profile, name="profile-page"),
]
