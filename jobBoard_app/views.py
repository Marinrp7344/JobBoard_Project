from typing import Any
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .models import *
from django.views import generic
from .forms import PostForm
from django.views.generic.edit import FormView

def index(request):
   return render( request, 'jobBoard_app/index.html')

def login(request):
   return HttpResponse('login')

def logout(request):
   return HttpResponse('logout')

def createPost(request):
    form = PostForm()
    if(request.method == 'POST'):
        post_data = request.POST.copy()
        form = PostForm(post_data)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('index')
        
    context = {'form':form}
    return render(request, 'jobBoard_app/post_form.html',context)

def updatePost(request, post_id):
    
    post = Post.objects.get(pk=post_id) 
    if(request.method == 'POST'):
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm(instance=post)  
    context = {'form':form}
    return render(request, 'jobBoard_app/post_update.html',context)

def deletePost(request, post_id):
    
    post = Post.objects.get(pk=post_id)
    if(request.method == 'POST'):
        post.delete()
        return redirect('index')

    return render(request, 'jobBoard_app/post_delete.html',{'post':post})

class PostListView(generic.ListView):
    model = Post
    def get_context_data(self,*args, **kwargs):
        visible_post = Post.objects.all().filter(is_visible=True)
        context = super(PostListView, self).get_context_data(*args,**kwargs)
        context['posts'] = visible_post
        return context

def about(request):
   return render( request, 'jobBoard_app/about.html')
