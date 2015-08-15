from django.shortcuts import render_to_response
from django.views.generic import View


class CadastroView(View):
    def __init__(self):
        self.template_name = 'core/cadastro.html'
        self.context = {}

    def get(self, request):
        return render_to_response(self.template_name, self.context)