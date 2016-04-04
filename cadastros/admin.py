from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Pessoa, Marca, Veiculo, Produto, Categoria, Centro_de_custo, Conta, Titulo

class PessoaForm(forms.ModelForm):
	class Meta:
		model = Pessoa
		fields = '__all__'
		labels = {
            'razao': _('Razão'),
        }

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
	"""docstring for PessoaAdmin"""
	search_fields = ['razao', 'fantasia']
	form = PessoaForm
# admin.site.register(Pessoa, PessoaAdmin)

class MarcaAdmin(admin.ModelAdmin):
	"""docstring for MarcaAdmin"""
	search_fields = ['descricao']
admin.site.register(Marca, MarcaAdmin)

class VeiculoAdmin(admin.ModelAdmin):
	"""docstring for VeiculoAdmin"""
	# fields = (('url', 'title'), 'content')
	list_display = ('placa', 'marca')
	list_filter = ['marca']
	search_fields = ['placa']
admin.site.register(Veiculo, VeiculoAdmin)

class ProdutoAdmin(admin.ModelAdmin):
	"""docstring for ProdutoAdmin"""
	search_fields = ['descricao']
admin.site.register(Produto, ProdutoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
	"""docstring for CategoriaAdmin"""
	search_fields = ['descricao']
admin.site.register(Categoria, CategoriaAdmin)

class Centro_de_custoAdmin(admin.ModelAdmin):
	"""docstring for Centro_de_custoAdmin"""
	search_fields = ['descricao']
admin.site.register(Centro_de_custo, Centro_de_custoAdmin)

class ContaAdmin(admin.ModelAdmin):
	"""docstring for ContaAdmin"""
	search_fields = ['descricao']
admin.site.register(Conta, ContaAdmin)

class TituloAdmin(admin.ModelAdmin):
	"""docstring for TituloAdmin"""
	search_fields = ['descricao']
admin.site.register(Titulo, TituloAdmin)