from django.forms import ModelForm
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#create class for project form
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields =('title', 'body', 'pay_rate','is_visible')