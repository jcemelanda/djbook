from django.test import SimpleTestCase
from django.contrib.auth.models import User


class CadastroTestCase(SimpleTestCase):
    def test_acessa_cadastro(self):
        response = self.client.get('/cadastro/')
        self.assertEqual(response.status_code, 200)

    def test_mostra_form(self):
        response = self.client.get('/cadastro/')
        self.assertContains(response, '<form')
        self.assertContains(response, 'name="usuario"')
        self.assertContains(response, 'name="senha1"')
        self.assertContains(response, 'name="senha2"')

    def test_send_empty_form_fails(self):
        data = {}
        response = self.client.post('/cadastro/', data)
        self.assertContains(response, 'This field is required.')

    def test_send_mismatching_psswd_fails(self):
        data = {
            'usuario': 'teste',
            'senha1': 'senha1',
            'senha2': 'senha2'
        }
        response = self.client.post('/cadastro/', data)
        self.assertContains(response, 'Senhas não conferem')

    def test_creation_works(self):
        usuarios = User.objects.count()
        data = {
            'usuario': 'teste',
            'senha1': 'senha1',
            'senha2': 'senha1'
        }
        self.client.post('/cadastro/', data)
        self.assertEqual(1, User.objects.count() - usuarios)

    def test_user_created_is_logged(self):
        data = {
            'usuario': 'teste1',
            'senha1': 'senha1',
            'senha2': 'senha1'
        }
        response = self.client.post('/cadastro/', data)
        self.assertTrue(response.wsgi_request.user.is_authenticated())

    def test_redirects_to_home(self):
        data = {
            'usuario': 'teste2',
            'senha1': 'senha1',
            'senha2': 'senha1'
        }
        response = self.client.post('/cadastro/', data)
        self.assertRedirects(response, '/')


class LoginTestCase(SimpleTestCase):
    def setUp(self):
        u, _ = User.objects.get_or_create(username='teste_login')
        u.set_password('senha')

    def test_acessa_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_mostra_form(self):
        response = self.client.get('/login/')
        self.assertContains(response, '<form')
        self.assertContains(response, 'name="usuario"')
        self.assertContains(response, 'name="senha"')

    def test_send_empty_form_fails(self):
        data = {}
        response = self.client.post('/login/', data)
        self.assertContains(response, 'This field is required.')

    def test_login_works(self):
        data = {
            'usuario': 'teste_login',
            'senha': 'senha'
        }
        response = self.client.post('/login/', data)
        self.assertTrue(response.wsgi_request.user.is_authenticated())