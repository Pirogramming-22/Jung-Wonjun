from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
]