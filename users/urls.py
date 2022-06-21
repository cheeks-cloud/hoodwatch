from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='users-signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='users/signin.html'), name='users-signin'),
    path('signout/', auth_views.LogoutView.as_view(), name='users-signout'),
    path('update_user', views.update, name='users-update-user')
]
