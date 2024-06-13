from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class AuthenticationUserTestCase(APITestCase):
    def setUp(self) -> None:
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('c3po', password='123456')

    def test_autenticacao_user_com_credenciais_corretas(self):
        """
        Verifica se a autenticação de usuário com credenciais válidas é bem-sucedida.

        Este teste tenta autenticar um usuário com o nome de usuário 'c3po' e a senha '123456'. 
        Ele espera que o resultado da função `authenticate` seja um objeto de usuário válido e que o usuário esteja autenticado.
        """
        user = authenticate(username='c3po', password='123456')
        self.assertTrue(user is not None and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self):
        """
        Verifica se uma requisição GET sem autenticação resulta em erro 401 Unauthorized.

        Este teste realiza uma requisição GET para a URL `self.list_url` sem fornecer credenciais de autenticação. 
        Espera-se que a resposta tenha o código de status HTTP 401 Unauthorized, indicando que a requisição não foi autorizada.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_autenticacao_user_com_username_incorreto(self):
        """
        Verifica se a autenticação com nome de usuário incorreto falha.

        Este teste tenta autenticar um usuário com um nome de usuário incorreto ('c3pp') e uma senha válida ('123456').
        Espera-se que a função `authenticate` retorne `None`, indicando que a autenticação falhou, e que o usuário não esteja autenticado.
        """
        user = authenticate(username='c3pp', password='123456')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_autenticacao_user_com_senha_incorreto(self):
        """
        Verifica se a autenticação com senha incorreta falha.

        Este teste tenta autenticar um usuário com um nome de usuário válido ('c3po') e uma senha incorreta ('123455').
        Espera-se que a função `authenticate` retorne `None`, indicando que a autenticação falhou, e que o usuário não esteja autenticado.
        """
        user = authenticate(username='c3po', password='123455')
        self.assertFalse(user is not None and user.is_authenticated)
