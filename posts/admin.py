from django.contrib import admin
# posts/admin.py

from .models import Post, Receita

admin.site.register(Post)
admin.site.register(Receita)

