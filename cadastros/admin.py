from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Pessoa, Marca, Veiculo, Produto, Categoria, Centro_de_custo, Conta, Titulo

# class MyAdmin(AdminSite):
admin.site_header = _('Oficina WEB')

# admin_site = MyAdmin(name='admin')

class PessoaForm(forms.ModelForm):
	class Meta:
		model = Pessoa
		fields = '__all__'
		labels = {
            'razao': _('Razão'),
            'inscricao_estadual': _('Inscrição Estadual'),
        }
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
	"""docstring for PessoaAdmin"""
	search_fields = ['razao', 'fantasia']
	form = PessoaForm
# admin_site.register(Pessoa, PessoaAdmin)

# class ClienteForm(forms.ModelForm):
# 	class Meta:
# 		model = Cliente
# 		fields = '__all__'
# 		labels = {
#             'razao': _('Razão'),
#             'inscricao_estadual': _('Inscrição Estadual'),
#         }
# @admin.register(Cliente)
# class ClienteAdmin(admin.ModelAdmin):
# 	"""docstring for ClienteAdmin"""
# 	search_fields = ['razao', 'fantasia']
# 	form = ClienteForm

# class FornecedorForm(forms.ModelForm):
# 	class Meta:
# 		model = Fornecedor
# 		fields = '__all__'
# 		labels = {
#             'razao': _('Razão'),
#             'inscricao_estadual': _('Inscrição Estadual'),
#         }
# @admin.register(Fornecedor)
# class FornecedorAdmin(admin.ModelAdmin):
# 	"""docstring for FornecedorAdmin"""
# 	search_fields = ['razao', 'fantasia']
# 	form = FornecedorForm

class MarcaForm(forms.ModelForm):
	class Meta:
		model = Marca
		fields = '__all__'
		labels = {
            'descricao': _('Descrição'),
        }
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
	"""docstring for MarcaAdmin"""
	search_fields = ['descricao']
	form = MarcaForm
# admin_site.register(Marca, MarcaAdmin)

class VeiculoForm(forms.ModelForm):
	class Meta:
		model = Veiculo
		fields = '__all__'
		labels = {
            'ano_fabricacao': _('Ano Fabricação'),
            'proprietario': _('Proprietário'),
        }
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
	"""docstring for VeiculoAdmin"""
	# fields = (('url', 'title'), 'content')
	list_display = ('placa', 'marca')
	list_filter = ['marca']
	search_fields = ['placa']
	form = VeiculoForm
# admin_site.register(Veiculo, VeiculoAdmin)

class ProdutoForm(forms.ModelForm):
	class Meta:
		model = Produto
		fields = '__all__'
		labels = {
			'codigo': _('Código'),
            'descricao': _('Descrição'),
            'estoque_minimo': _('Estoque Mínimo'),
            'preco': _('Preço'),
        }
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
	"""docstring for ProdutoAdmin"""
	search_fields = ['descricao']
	form = ProdutoForm
# admin_site.register(Produto, ProdutoAdmin)

class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = '__all__'
		labels = {
            'descricao': _('Descrição'),
        }
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	"""docstring for CategoriaAdmin"""
	search_fields = ['descricao']
	form = CategoriaForm
# admin_site.register(Categoria, CategoriaAdmin)

class Centro_de_custoForm(forms.ModelForm):
	class Meta:
		model = Centro_de_custo
		fields = '__all__'
		labels = {
            'descricao': _('Descrição'),
        }
@admin.register(Centro_de_custo)
class Centro_de_custoAdmin(admin.ModelAdmin):
	"""docstring for Centro_de_custoAdmin"""
	search_fields = ['descricao']
	form = Centro_de_custoForm
# admin_site.register(Centro_de_custo, Centro_de_custoAdmin)

class ContaForm(forms.ModelForm):
	class Meta:
		model = Conta
		fields = '__all__'
		labels = {
            'descricao': _('Descrição'),
        }
@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
	"""docstring for ContaAdmin"""
	search_fields = ['descricao']
	form = ContaForm
# admin_site.register(Conta, ContaAdmin)

class TituloForm(forms.ModelForm):
	class Meta:
		model = Titulo
		fields = '__all__'
		labels = {
            'descricao': _('Descrição'),
            'codigo': _('Código'),
            'emissao': _('Emissão'),
        }
@admin.register(Titulo)
class TituloAdmin(admin.ModelAdmin):
	"""docstring for TituloAdmin"""
	search_fields = ['descricao']
	form = TituloForm
# admin_site.register(Titulo, TituloAdmin)