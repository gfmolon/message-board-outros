# posts/tests.py

from django.test import TestCase
from django.urls import reverse

from .models import Post, Receita, Produto


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")
        cls.receita = Receita.objects.create(text="This is a teste!")
        cls.produto = Produto.objects.create(
            nome="Teste",
            descricao="Teste",
            preco=1.0,
            estoque=1,
            imagem_pequena="1",
            imagem_grande="1",
        )

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")
        self.assertEqual(self.receita.text, "This is a teste!")
        self.assertEqual(self.produto.nome, "Teste")
        self.assertEqual(self.produto.descricao, "Teste")
        self.assertEqual(self.produto.preco, 1.0)
        self.assertEqual(self.produto.imagem_pequena, "1")
        self.assertEqual(self.produto.imagem_grande, "1")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_receitas_location(self):
        response = self.client.get("/receitas/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_produtos_location(self):
        response = self.client.get("/produtos/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")
        self.assertContains(response, "This is a test!")

    def test_receitas(self):
        response = self.client.get(reverse("receitas"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "receita_list.html")
        self.assertContains(response, "This is a teste!")

    def test_produtos(self):
        response = self.client.get(reverse("lista_produtos"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "produto_list.html")
        self.assertContains(response, "Teste")
