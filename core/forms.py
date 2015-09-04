from django.forms import Form
from django.forms import EmailField
from django.forms import CharField
from django.forms import PasswordInput


class CadastroForm(Form):
    email = EmailField(label='e-mail')
    senha1 = CharField(label='senha', widget=PasswordInput)
    senha2 = CharField(label='confirmação de senha', widget=PasswordInput)
