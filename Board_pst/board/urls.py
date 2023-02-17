from django.urls import path
from .views import PostsList, PostDetail, PostCreate


urlpatterns = [
    path('', PostsList.as_view(), name='posts_list'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
]






















