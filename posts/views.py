# posts/views.py

# from django.shortcuts import render
# from .models import Post


# def post_list(request):
#    posts = Post.objects.all()
#    return render(request, "post_list.html", {"posts":posts})

from django.views.generic import ListView
from .models import Post, Receita, Produto
from django.shortcuts import render, redirect
from django.forms import modelform_factory


class PostList(ListView):
    model = Post
    template_name = "post_list.html"


class ReceitaList(ListView):
    model = Receita
    template_name = "receita_list.html"


ProdutoForm = modelform_factory(
    Produto,
    fields=[
        "ordem",
        "nome",
        "descricao",
        "preco",
        "estoque",
        "imagem_pequena",
        "imagem_grande",
    ],
)


class ProdutoList(ListView):
    model = Produto
    template_name = "produto_list.html"
    context_object_name = "produtos"
    ordering = ["-ordem"]


def cadastrar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cadastrar_produto")  # ou outra página
    else:
        form = ProdutoForm()
    return render(request, "produtos/cadastrar.html", {"form": form})
