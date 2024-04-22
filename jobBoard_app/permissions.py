from django.contrib.auth.models import User
from .models import Post,Client

def can_edit(request, post):

    if(request.user == post.client.user):
        return True
    else:
        return False
