from django.contrib import admin

# posts/admin.py

from .models import Post, Receita, Produto

admin.site.register(Post)
admin.site.register(Receita)
admin.site.register(Produto)
