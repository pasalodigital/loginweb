from django.http import HttpResponse
from presentation.base.views import BaseView

class DashboardView(BaseView):

    def get(self,request):
        return HttpResponse("hola")