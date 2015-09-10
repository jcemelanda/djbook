from django.conf.urls import url
from core.views import CadastroView
from core.views import LoginView
from core.views import HomeView

urlpatterns = [
    url(r'^cadastro/$', CadastroView.as_view(), name='cadastro'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^$', HomeView.as_view(), name='home'),
]