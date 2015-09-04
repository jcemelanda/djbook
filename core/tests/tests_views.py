from django.test import SimpleTestCase


class CadastroTestCase(SimpleTestCase):
    def test_acessa_cadastro(self):
        response = self.client.get('/cadastro/')
        self.assertEqual(response.status_code, 200)

    def test_mostra_form(self):
        response = self.client.get('/cadastro/')
        self.assertContains(response, '<form')
        self.assertContains(response, 'name="email"')
        self.assertContains(response, 'name="senha1"')
        self.assertContains(response, 'name="senha2"')

    def test_send_empty_form_fails(self):
        data = {}
        response = self.client.post(' /cadastro', data)
        self.assertContains(response, 'This field is required.')
    