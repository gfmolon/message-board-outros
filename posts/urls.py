from django.urls import path
from .views import PostList, ReceitaList, ProdutoList

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("receitas/", ReceitaList.as_view(), name="receitas"),
    path("produtos/", ProdutoList.as_view(), name="lista_produtos"),  # <- novo caminho
]
