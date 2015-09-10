from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from core.forms import CadastroForm
from core.forms import LoginForm


class CadastroView(View):
    def __init__(self):
        self.template_name = 'core/cadastro.html'
        self.context = {}

    def get(self, request):
        self.context['form'] = CadastroForm()
        return render_to_response(self.template_name,
                                  self.context,
                                  RequestContext(request))

    def post(self, request):
        form = CadastroForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['usuario'],
                                     password=form.cleaned_data['senha1'])
            u = authenticate(username=form.cleaned_data['usuario'],
                             password=form.cleaned_data['senha1'])
            login(request, u)
            return redirect("home")
        self.context['form'] = form
        return render_to_response(self.template_name,
                                  self.context,
                                  RequestContext(request))


class HomeView(View):
    def get(self, request):
        return render_to_response('core/home.html', {}, RequestContext(request))


class LoginView(View):
    def __init__(self):
        self.template_name = 'core/login.html'
        self.context = {}

    def get(self, request):
        self.context['form'] = LoginForm()
        return render_to_response(self.template_name,
                                  self.context,
                                  RequestContext(request))

    def post(self, request):
        form = LoginForm(request.POST)
        self.context['form'] = form
        if form.is_valid():
            u = authenticate(username=form.cleaned_data['usuario'],
                             password=form.cleaned_data['senha'])
            login(request, u)
        return render_to_response(self.template_name,
                                  self.context,
                                  RequestContext(request))