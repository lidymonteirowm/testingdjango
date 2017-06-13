from django.test import TestCase


class NoticiaTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/noticia/')

    def test_get(self):
        """GET /noticia/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use noticia/noticia.html"""
        self.assertTemplateUsed(self.response, 'noticias/noticia.html')


