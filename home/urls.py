from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('breakfast-detail/', views.breakfast_detail, name='detail'),
    path('breakfast-create/', views.breakfast_create, name='breakfast_create')
]