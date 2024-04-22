
from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            print('role',allowed_roles)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You can not see this page')
           
        return wrapper_func
    return decorator


def check_editable(request):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.client.user.has_perm("can_access"):
                print("Continue")
            else:
                return HttpResponse('You can not see this page')
           
        return wrapper_func
    return decorator