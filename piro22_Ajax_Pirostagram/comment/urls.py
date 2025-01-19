from django.urls import path
from comment import views

app_name = 'comment'

urlpatterns = [
    path('<int:post_id>/comment/', views.create, name='comment_create'),
]