from django.test import TestCase
from aluraflix.models import Programa


class ProgramaModelTestCase(TestCase):
    """
    Conjunto de testes para verificar o comportamento e atributos do modelo Programa.
    """

    def setUp(self):
        """
        Método de preparação executado antes de cada teste.

        Cria uma instância da classe Programa com dados de teste e define valores padrão para tipo, likes e dislikes.
        """
        self.programa = Programa(
            titulo='Procurando ninguém em latim',
            data_lancamento='2003-07-04'
        )
        self.default_tipo = 'F'
        self.default_likes = 0
        self.default_dislikes = 0

    def test_verifica_atributos_do_programa(self):
        """
        Verifica se os atributos do programa após a criação são os esperados.

        Este teste compara os valores dos atributos do programa (titulo, data_lancamento, tipo, likes, dislikes) 
        com os valores esperados definidos no método setUp.
        """
        self.assertEqual(self.programa.titulo, 'Procurando ninguém em latim')
        self.assertEqual(self.programa.data_lancamento, '2003-07-04')
        self.assertEqual(self.programa.tipo, self.default_tipo)
        self.assertEqual(self.programa.likes, self.default_likes)
        self.assertEqual(self.programa.dislikes, self.default_dislikes)
