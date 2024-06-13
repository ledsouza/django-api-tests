from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase


class AuthenticationUserTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user('c3po', password='123456')

    def test_autenticacao_user_com_credenciais_corretas(self):
        """
        Verifica se a autenticação de usuário com credenciais válidas é bem-sucedida.

        Este teste tenta autenticar um usuário com o nome de usuário 'c3po' e a senha '123456'. 
        Ele espera que o resultado da função `authenticate` seja um objeto de usuário válido e que o usuário esteja autenticado.
        """
        user = authenticate(username='c3po', password='123456')
        self.assertTrue(user is not None and user.is_authenticated)
