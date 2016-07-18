from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

class BaseView(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'