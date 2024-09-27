from django.db import models

# Modelo para a tabela tcategoria
class Categoria(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'tcategoria'  # Nome exato da tabela no banco de dados
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


# Modelo para a tabela tcliente
class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    senha = models.CharField(max_length=255)
    numero_telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.TextField(null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    numero_casa = models.CharField(max_length=10, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'tcliente'  # Nome exato da tabela no banco de dados
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


# Modelo para a tabela tusuarioadm
class UsuarioAdm(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome_fantasia = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=20)
    senha = models.CharField(max_length=255)
    numero_telefone = models.CharField(max_length=15)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'tusuarioadm'  # Nome exato da tabela no banco de dados
        verbose_name = 'Usuário Administrador'
        verbose_name_plural = 'Usuários Administradores'


# Modelo para a tabela tpedido
class Pedido(models.Model):
    codigo = models.AutoField(primary_key=True)
    numero_pedido = models.CharField(max_length=255)
    cod_usuario_adm = models.ForeignKey(UsuarioAdm, on_delete=models.CASCADE, related_name='pedidos')
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    situacao = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        db_table = 'tpedido'  # Nome exato da tabela no banco de dados
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


# Modelo para a tabela tpedidoitem
class PedidoItem(models.Model):
    codigo = models.AutoField(primary_key=True)
    cod_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    cod_produto = models.ForeignKey('Produto', on_delete=models.CASCADE, related_name='itens')
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'tpedidoitem'  # Nome exato da tabela no banco de dados
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'


# Modelo para a tabela tproduto
class Produto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)
    codigo_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    observacoes = models.TextField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tproduto'  # Nome exato da tabela no banco de dados
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'