from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
  model: Produto
  list_display = ['nome', 'preco', 'img']
  search_fields = ['nome']
  save_on_top = True

admin.site.register(Produto, ProdutoAdmin)
