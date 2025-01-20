from django.urls import path
from comment import views

app_name = 'comment'

urlpatterns = [
    path('<int:post_id>/comment/', views.comment, name='comment'),
    path('<int:post_id>/delete/<int:pk>', views.delete, name='delete'),
]