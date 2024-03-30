from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
   return render( request, 'jobBoard_app/index.html')

def login(request):
   return HttpResponse('login')

def logout(request):
   return HttpResponse('logout')