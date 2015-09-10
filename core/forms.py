from django.forms import Form
from django.forms import CharField
from django.forms import PasswordInput
from django.forms import ValidationError


class CadastroForm(Form):
    usuario = CharField(label='usuario', max_length=30)
    senha1 = CharField(label='senha', widget=PasswordInput)
    senha2 = CharField(label='confirmação de senha', widget=PasswordInput)

    def clean_senha2(self):
        p1 = self.cleaned_data['senha1']
        if self.cleaned_data['senha2'] != p1:
            raise ValidationError('Senhas não conferem')
        return p1


class LoginForm(Form):
    usuario = CharField(label='usuario', max_length=30)
    senha = CharField(label='confirmação de senha', widget=PasswordInput)
