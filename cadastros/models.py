from django.db import models
import datetime

class Pessoa(models.Model):
	"""Cadastro de Pessoas"""
	razao = models.CharField(max_length=120, blank=False)
	fantasia = models.CharField(max_length=120, blank=True)
	cnpj = models.CharField(max_length=20, blank=True)
	cpf = models.CharField(max_length=20, blank=True)
	inscricao_estadual = models.CharField(max_length=20, blank=True)
	rg = models.CharField(max_length=20, blank=True)
	telefone = models.CharField(max_length=20, blank=True)
	obs = models.TextField(blank=True)
	def __str__(self):
		return self.razao

class Marca(models.Model):
	"""Cadastro de Marcas"""
	descricao = models.CharField(max_length=120, blank=False)
	def __str__(self):
		return self.descricao

class Veiculo(models.Model):
	"""Cadastro de Veiculos"""
	placa = models.CharField(max_length=10, blank=False)
	ano_fabricacao = models.IntegerField(blank=True, null=True)
	ano_modelo = models.IntegerField(blank=True, null=True)
	renavam = models.CharField(max_length=60, blank=True)
	chassi = models.CharField(max_length=60, blank=True)
	marca = models.ForeignKey(Marca, null=True, blank=True, on_delete=models.PROTECT)
	proprietario = models.ForeignKey(Pessoa, null=True, blank=True, on_delete=models.PROTECT)

class Produto(models.Model):
	"""Cadastro de Produtos"""
	codigo = models.CharField(max_length=60, blank=True)
	descricao = models.CharField(max_length=120, blank=False)
	estoque_minimo = models.IntegerField(blank=True, null=True)
	saldo = models.IntegerField(blank=True, null=True)
	preco = models.DecimalField(max_digits=15, decimal_places=2, default=0)
	def __str__(self):
		return self.descricao

class Categoria(models.Model):
	"""Cadastro de Categorias"""
	descricao = models.CharField(max_length=120, blank=False)
	def __str__(self):
		return self.descricao

class Centro_de_custo(models.Model):
	"""Cadastro de Centro de Custo"""
	descricao = models.CharField(max_length=120, blank=False)
	def __str__(self):
		return self.descricao

class Conta(models.Model):
	"""Cadastro de Contas"""
	descricao = models.CharField(max_length=120, blank=False)
	saldo_inicial = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=False, default=0)
	def __str__(self):
		return self.descricao

class Titulo(models.Model):
	"""Cadastro de Títulos"""
	codigo = models.CharField(max_length=60, blank=True)
	descricao = models.CharField(max_length=120, blank=False)
	emissao = models.DateField(null=True, blank=True, default=datetime.date.today)
	vencimento = models.DateField(null=False, blank=False, default=datetime.date.today)
	PAGAR = 'P'
	RECEBER = 'R'
	TIPO_OPCAO = (
		(PAGAR, 'PAGAR'),
		(RECEBER, 'RECEBER'),
	)
	tipo = models.CharField(max_length=1, choices=TIPO_OPCAO, blank=False, null=False)
	conta = models.ForeignKey(Conta, null=True, blank=True, on_delete=models.PROTECT)
	pessoa = models.ForeignKey(Pessoa, null=True, blank=True, on_delete=models.PROTECT)
	categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.PROTECT)
	centro_de_custo = models.ForeignKey(Centro_de_custo, null=True, blank=True, on_delete=models.PROTECT)
	valor = models.DecimalField(max_digits=15, decimal_places=2)
	valor_desconto = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
	valor_juros = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
	valor_pago = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
	def __str__(self):
		return self.descricao

class Movimentos(models.Model):
	"""Lançamentos financeiros"""
	conta = models.ForeignKey(Conta, null=False, blank=False, on_delete=models.PROTECT)
	valor = models.DecimalField(max_digits=15, decimal_places=2)
	data = models.DateField(null=False, blank=False, default=datetime.date.today)
