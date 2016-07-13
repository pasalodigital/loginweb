from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import View, FormView

from presentation.public.forms import *


def index(request):
    return TemplateResponse(request, 'public/templates/index.html')


class RegistrarView(FormView):

    form_class = RegistrarUsuarioForm
    template_name = 'public/templates/usuario_registrar.html'
    success_url = '/'

    def form_valid(self, form):
        valid = super(RegistrarView, self).form_valid(form)
        userForm = form.save(commit=False)
        user = User.objects.create_user(userForm.username, userForm.email, userForm.password)
        authUser = authenticate(username=user.username, password=user.password)
        if authUser is not None:
            if authUser.is_active:
                login(self.request, authUser)
            else:
                print('usuario no activo')
        else:
            print('usuario no encontrado')
        return HttpResponse("correcto")


class LoginView(View):

    def get(self, request):
        form = LoginUsuarioForm()
        return TemplateResponse(request, 'public/templates/usuario_login.html', {'form': form})

    def post(self,request):
        form = LoginUsuarioForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponse('correcto')
        else:
            return TemplateResponse(request, 'usuario_login.html', {'form': form})