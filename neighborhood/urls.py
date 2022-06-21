from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='neighborhood-home'),
    path('create_business/', views.create_business, name='neighborhood-create-business'),
    path('create_hood/', views.create_hood, name='neighborhood-create-hood'),
    path('create_post/', views.create_post, name='neighborhood-create-post'),
    path('join_hood/', views.join_hood, name='neighborhood-join-hood')
]
