from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from core.forms import CadastroForm


class CadastroView(View):
    def __init__(self):
        self.template_name = 'core/cadastro.html'
        self.context = {}

    def get(self, request):
        self.context['form'] = CadastroForm()
        return render_to_response(self.template_name, self.context, RequestContext(request))

    def post(self, request):
        self.context['form'] = CadastroForm(request.POST)
        return render_to_response(self.template_name, self.context, RequestContext(request))