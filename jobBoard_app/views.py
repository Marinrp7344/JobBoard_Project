from typing import Any
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .models import *
from django.views import generic
from .forms import PostForm,CreateUserForm
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user, check_editable
from .permissions import can_edit
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from serpapi import GoogleSearch

def index(request):
   return render( request, 'jobBoard_app/index.html')

def login(request):
   return HttpResponse('login')

def logout(request):
   return HttpResponse('logout')

@login_required(login_url='login')
def createPost(request):
    form = PostForm()
    if(request.method == 'POST'):
        post_data = request.POST.copy()
        form = PostForm(post_data)
        if form.is_valid():
            post = form.save(commit=False)
            client = Client.objects.filter(user=request.user)
            post.client = client[0]
            post.save()


            return redirect('index')
       
    context = {'form':form}
    return render(request, 'jobBoard_app/post_form.html',context)



def updatePost(request, post_id):
    currentUser = request.user
    post = Post.objects.get(pk=post_id)
    if(currentUser == post.client.user):
        print("user is true")
        print(currentUser.has_perm("post.can_access"))
        if(request.method == 'POST'):
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = PostForm(instance=post)  
        context = {'form':form}
        return render(request, 'jobBoard_app/post_update.html',context)
    else:
        return render(request, 'jobBoard_app/invalid_user.html')


def deletePost(request, post_id):
    currentUser = request.user
    post = Post.objects.get(pk=post_id)
    if(currentUser == post.client.user):
        if(request.method == 'POST'):
            post.delete()
            return redirect('index')

        return render(request, 'jobBoard_app/post_delete.html',{'post':post})
    else:
        return render(request, 'jobBoard_app/invalid_user.html')

class PostListView(generic.ListView):
    model = Post
    def get_context_data(self,*args, **kwargs):
        visible_post = Post.objects.all().filter(is_visible=True)
        context = super(PostListView, self).get_context_data(*args,**kwargs)
        context['posts'] = visible_post
        context['user'] = self.request.user
        return context

class PostDetailView(generic.DetailView):
    model = Post
    

def about(request):
   return render( request, 'jobBoard_app/about.html')


def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='client_role')
            user.groups.add(group)
            client = Client.objects.create(user=user)
            client.save()


            messages.success(request, "Account was created for " + username)
            return redirect('login')
   
    context = {'form':form}
    return render(request,'registration/register.html',context)

def findString(res):
    textResults = str(res.text)
    text = []
    for result in textResults:
        if(ord(result) != 10):
            text.append(result)


    stringText = ""
    newString = ""
    for chr in text:
        newString = newString + stringText.join(chr)
    print(newString)
    return newString


def searchPage(searchItem):
    driver_options = Options()
    driver_options.add_argument('--headless')
    driver = webdriver.Chrome()
    driver.get("https://www.homedepot.com/")
    time.sleep(5)

    results = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/div[1]/form/div[1]/input")
    results.send_keys(searchItem)
    results.send_keys(webdriver.Keys.ENTER)


    searchResults1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[6]/div[2]/div[1]/div/section[1]/div[1]/div/div[3]/div[2]/div/div/div/div/div")
    searchResults2 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[6]/div[2]/div[1]/div/section[1]/div[2]/div/div[3]/div[2]/div/div/div/div/div[1]")
    searchResults3 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[6]/div[2]/div[1]/div/section[1]/div[3]/div/div[3]/div[2]/div/div/div/div/div")
    searchName1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[6]/div[2]/div[1]/div/section[1]/div[1]/div/div[3]/div[5]/div/a/div/h3/p")
    searchName2 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[6]/div[2]/div[1]/div/section[1]/div[2]/div/div[3]/div[5]/div/a/div/h3/p")
    searchName3 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[6]/div[2]/div[1]/div/section[1]/div[3]/div/div[3]/div[5]/div/a/div/h3/p")
    
    searchLink1Element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[6]/div[2]/div[1]/div/section[1]/div[1]/div/a")
    searchlink1 = searchLink1Element.get_attribute("href")
    searchLink2Element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[6]/div[2]/div[1]/div/section[1]/div[2]/div/a")
    searchlink2 = searchLink2Element.get_attribute("href")
    searchLink3Element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[6]/div[2]/div[1]/div/section[1]/div[3]/div/a")
    searchlink3 = searchLink3Element.get_attribute("href")
    time.sleep(10)
    items = [findString(searchName1),findString(searchResults1),findString(searchName2),findString(searchResults2), findString(searchName3),findString(searchResults3),searchlink1,searchlink2,searchlink3]
    #prices2 = [findString(searchResults1),findString(searchResults2),findString(searchResults3)]
    print(items)
    print(driver.current_url)
    driver.close()
    driver.quit()
    return items

def displayTools(request, tool_name):
    print(tool_name)
    items= searchPage(tool_name)
    tool1Name = items[0]
    tool1Price = items[1]
    tool2Name = items[2]
    tool2Price = items[3]
    tool3Name = items[4]
    tool3Price = items[5]
    tool1Link = items[6]
    tool2Link = items[7]
    tool3Link = items[8]
    print(items)

    context = {
        'tool1Name': tool1Name,
        'tool1Price': tool1Price,
        'tool2Name': tool2Name,
        'tool2Price': tool2Price,
        'tool3Name': tool3Name,
        'tool3Price': tool3Price,
        'tool1Link': tool1Link,
        'tool2Link': tool2Link,
        'tool3Link': tool3Link,
    }
    return render(request,'jobBoard_app/display_tools.html',context)

def apiDisplayTools(request, tool_name):
    params = {
    "engine": "home_depot",
    "q": tool_name,
    "api_key": "27ef68dde03b5d95f340b538dc31441f3756b8ac2ea5937c329073761826c0ce"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    products = results["products"]

    for product in products:
        print(product['title'])
        print(product['link'])
        print(product['price'])
        print("---------------------------")
    context = {'products':products}
    return render(request,'jobBoard_app/display_tools_api.html',context)
