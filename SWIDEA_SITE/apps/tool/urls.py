from django.urls import path
from apps.tool import views

app_name = 'tool'

urlpatterns = [
    path('tool/list', views.list, name='list'),
    path('tool/detail/<int:pk>', views.detail, name='detial'),
    path('tool/create', views.create, name='create'),
    path('tool/update/<int:pk>', views.update, name='update'),
]