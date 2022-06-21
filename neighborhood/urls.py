from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='neighborhood-home'),
    path('create_business', views.create_business, name='neighborhood-create-business')
]
