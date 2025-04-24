# posts/tests.py

from django.test import TestCase
from django.urls import reverse

from .models import Post, Receita


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")
        cls.receita = Receita.objects.create(text="This is a teste!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")
        self.assertEqual(self.receita.text, "This is a teste!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)
    
    def test_url_exists_at_receitas_location(self):
        response = self.client.get("/receitas/")
        self.assertEqual(response.status_code,200)

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")
        self.assertContains(response,"This is a test!")
    
    def test_receitas(self):
        response = self.client.get(reverse("receitas"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "receita_list.html")
        self.assertContains(response,"This is a teste!")


