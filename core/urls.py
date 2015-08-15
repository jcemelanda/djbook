from django.conf.urls import url
from core.views import CadastroView

urlpatterns = [
    url(r'^cadastro/$', CadastroView.as_view(), name='cadastro'),
]