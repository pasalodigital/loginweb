from django.conf.urls import url

from presentation.public.views import *
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registrar/$', RegistrarView.as_view(), name='public.usuario.registrar'),
    url(r'^login/$', LoginView.as_view(), name='public.usuario.login'),
]