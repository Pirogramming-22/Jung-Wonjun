from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    # 리스트 페이지
    path('', board_list, name='board_list'),

    # 디테일 페이지
    path('detail/<int:pk>', board_detail, name='board_detail'),

    # 리뷰 작성 페이지
    path('create', board_create, name='board_create'),

    # 리뷰 수정 페이지
    path('update/<int:pk>', board_update, name='board_update'),

    # 리뷰 삭제
    path('delete/<int:pk>', board_delete, name='board_delete'),
]