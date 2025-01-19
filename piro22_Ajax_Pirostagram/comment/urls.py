from django.urls import path
from comment import views

app_name = 'comment'

urlpatterns = [
    path('<int:post_id>/comment/list', views.list, name='list'),
    path('<int:post_id>/comment/create', views.create, name='create'),
]