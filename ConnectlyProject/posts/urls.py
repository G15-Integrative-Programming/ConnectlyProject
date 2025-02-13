from django.urls import path
from . import views
from .views import UserListCreate, PostListCreate, CommentListCreate

urlpatterns = [
    #path('users/create/', views.create_user, name='create_user'),
    #path('posts/create/', views.create_post, name='create_post'),
    #path('users/', UserListCreate.as_view(), name='user-list-create'), 
    #path('posts/', PostListCreate.as_view(), name='post-list-create'), 
    #path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('users/', views.UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('posts/', views.PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('comments/', views.CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
]