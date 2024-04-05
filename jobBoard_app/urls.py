from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.login, name='login'),
    path('', views.logout, name='logout'),
    path('create_post/', views.createPost,name='create-post'),
    path('posts/', views.PostListView.as_view(), name= 'posts'),
    path('posts/<int:post_id>/update_post/', views.updatePost,name='update-post'),
    path('posts/<int:post_id>/delete_post/', views.deletePost,name='delete-post'),
    path('about/', views.about, name='about'),
]