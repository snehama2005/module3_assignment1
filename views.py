# from django.shortcuts import render
# from django.views.generic.edit import CreateView
# from.models import GreekModel

# class GreekCreate(CreateView):
#     model=GreekModel
#     fields=['title','description']
#     template_name='geekmodel_form.html'

# # Create your views here.
from django.db import models

# Create your models here.
# from django.shortcuts import render
# from django.views.generic.edit import CreateView
# from.models import LoginModel

# class LoginCreate(CreateView):
    # model=LoginModel
    # fields=["username","password"]
    # template_name="loginmodel_form.html"
from django.views.generic.list import ListView
from .models import LoginModel
class LoginList(ListView):
    model=LoginModel
    template_name='loginmodel_list.html'
    context_object_name='login_list'
    

