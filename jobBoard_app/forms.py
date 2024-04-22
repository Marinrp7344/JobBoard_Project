from django.forms import ModelForm
from .models import Post, Client
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#create class for project form
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields =('title', 'body', 'description', 'tools', 'pay_rate','is_visible')


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['user']