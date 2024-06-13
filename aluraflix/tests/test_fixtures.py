from django.test import TestCase
from aluraflix.models import Programa


class FixtureDataTestCase(TestCase):

    fixtures = ['programas_iniciais']

    def test_verifica_carregamento_da_fixture(self):
        """
        Verifica se os dados da fixture foram carregados corretamente no banco de dados de teste.

        Este teste busca um programa específico pelo ID 1 e verifica se seu título é 'Coisas bizarras'. 
        Em seguida, obtém todos os programas do banco de dados e verifica se a quantidade total é 9.

        Este teste é útil para garantir que seus dados de teste (fixtures) estão sendo carregados corretamente antes de executar outros testes.
        """
        programa_1 = Programa.objects.get(pk=1)
        todos_programas = Programa.objects.all()
        self.assertEqual(programa_1.titulo, 'Coisas bizarras')
        self.assertEqual(len(todos_programas), 9)
