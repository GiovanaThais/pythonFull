from datetime import datetime


class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produto(Categoria):
    def __init__(self, preco, nomeProduto, categoria):
        self.preco = preco
        self.nomeProduto = nomeProduto
        super(Produto, self).__init__(categoria)

class Estoque:
    def __init__(self, quantidade, produto: Produto):
        self.quantidade = quantidade
        self.produto = produto

class Venda:
    def __init__(self, itensVendido: Produto, vendedor, comprador,
                    quantVendida, data = datetime.now().strftime("%d/%m/%Y")):
        self.itensVendido = itensVendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantVendida = quantVendida
        self.data = data

class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco

# class Pessoa(Base):
#         __tablename__ = 'Pessoa'
#         id = Column(Integer, primary_key = True)
#         nome = Column(String(50))
        # usuario = Column(String(20))
#         senha = Column(String(10))
#         idCategoria = Column(Integer, ForeignKey('categoria.id))


class Funcionario(Pessoa):
    def __init__(self, clt, nome, telefone, cpf, email, endereco):
        self.clt = clt
        super(Funcionario, self).__init__(nome, telefone, cpf, email, endereco)
        

class Fornecedor(Pessoa):
    def __init__(self, cnpj, telefone, nome, categoria ):
        self.cnpj = cnpj
        self.categoria = categoria
        super(Fornecedor, self).__init__(telefone, nome)
