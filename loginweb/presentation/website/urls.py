from django.conf.urls import url

from presentation.website.views import *
from . import views

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='public.website.dashboard')
]