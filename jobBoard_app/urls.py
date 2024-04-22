from django.urls import path,include
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.login, name='login'),
    path('', views.logout, name='logout'),
    path('create_post/', views.createPost,name='create-post'),
    path('posts/', views.PostListView.as_view(), name= 'posts'),
    path('posts/post/<int:pk>', views.PostDetailView.as_view(), name= 'post-detail'),
    path('posts/<int:post_id>/update_post/', views.updatePost,name='update-post'),
    path('posts/<int:post_id>/delete_post/', views.deletePost,name='delete-post'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/',views.registerPage, name = 'register_page'),
    path('tools/<str:tool_name>', views.displayTools, name='display-tools'),
    path('tool/<str:tool_name>', views.apiDisplayTools, name='display-tools-api')
    
]