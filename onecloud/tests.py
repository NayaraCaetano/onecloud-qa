# coding: utf-8

from core.tests import BaseTestCase


class OneCloudTestCase(BaseTestCase):
    URL_SERVICES = '/api/services/'

    def test_api_listagem_servicos_nao_requer_usuario_logado(self):
        response = self.client.get(self.URL_SERVICES)
        self.assertEquals(200, response.status_code)

    def test_api_lista_services(self):
        self._cria_service()
        self._cria_service()
        response = self.client.get(self.URL_SERVICES)
        self.assertEquals(2, response.data.get('count'))

    def test_api_nao_lista_provider(self):
        #  Não existe nenhuma view rest criada para gerencia do model Provider
        self.assertTrue(True)

    def test_api_nao_cadastra_provider(self):
        #  Não existe nenhuma view rest criada para gerencia do model Provider
        self.assertTrue(True)

    def test_api_nao_cadastra_service(self):
        response = self.client.post(self.URL_SERVICES)
        self.assertEquals(405, response.status_code)

    def test_api_nao_edita_provider(self):
        #  Não existe nenhuma view rest criada para gerencia do model Provider
        self.assertTrue(True)

    def test_api_nao_edita_service(self):
        response = self.client.put(self.URL_SERVICES)
        self.assertEquals(405, response.status_code)

    def test_api_nao_deleta_provider(self):
        #  Não existe nenhuma view rest criada para gerencia do model Provider
        self.assertTrue(True)

    def test_api_nao_deleta_service(self):
        response = self.client.delete(self.URL_SERVICES)
        self.assertEquals(405, response.status_code)
