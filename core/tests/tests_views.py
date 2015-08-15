from django.test import SimpleTestCase


class CadastroTestCase(SimpleTestCase):
    def test_acessa_cadastro(self):
        response = self.client.get('/cadastro/')
        self.assertEqual(response.status_code, 200)