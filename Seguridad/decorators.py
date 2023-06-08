from django.http import HttpResponse
from django.shortcuts import render, redirect


def authenticated_user(view_func):
    def wrapper_func(request,  *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/main')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_groups = []):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
                #'flat = true' retorna el valor 'limpio' del QuerySet
                user_groups = request.user.groups.values_list('name', flat=True)
                if any(group in user_groups for group in allowed_groups):
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('/main')
        return wrapper_func
    return decorator