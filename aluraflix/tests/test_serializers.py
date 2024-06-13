from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.programa = Programa(
            titulo='Procurando ninguém em latim',
            data_lancamento='2003-07-04',
            tipo='F',
            likes=2340,
            dislikes=40
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verifica_campos_serializados(self):
        """
        Verifica se a serialização do programa inclui os campos esperados.

        Este teste serializa a instância de `Programa` e verifica se os campos 'titulo', 'tipo', 'data_lancamento' e 'likes' 
        estão presentes nos dados serializados. O campo 'dislikes' não é incluído na serialização por padrão.

        A comparação é feita utilizando conjuntos para garantir que a ordem dos campos não afete o resultado do teste.
        """
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(
            ['titulo', 'tipo', 'data_lancamento', 'likes']))
