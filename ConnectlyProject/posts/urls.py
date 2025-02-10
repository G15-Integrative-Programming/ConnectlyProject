from django.urls import path
from . import views
from .views import UserListCreate, PostListCreate, CommentListCreate

urlpatterns = [
    #path('users/create/', views.create_user, name='create_user'),
    #path('posts/create/', views.create_post, name='create_post'),
    path('users/', UserListCreate.as_view(), name='user-list-create'), 
    path('posts/', PostListCreate.as_view(), name='post-list-create'), 
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
]