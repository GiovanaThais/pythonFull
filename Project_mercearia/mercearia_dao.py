from mercearia_model import Categoria, Estoque, Funcionario, Pessoa, Produto, Fornecedor, Venda


class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categorias.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('categorias.txt','r') as arq:
            cls.categorias = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categorias))

        categ = []
        for i in cls.categoria:
            categ.append(Categoria(i))
        return categ

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produto, quantidade: str):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + ' ' + produto.preco+ ' ' +
                            produto.categoria+ ' ' +str(quantidade))
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('estoque.txt','r') as arq:
            cls.estoque = arq.readlines()
        
        cls.estoque = list(map(lambda x: x.replace('\n',''), cls.estoque))

        est = []
        if len(cls.estoque) > 0:
            for i in cls.est:
                est.append(Estoque(Produto(i[0], i[1], i[2], i[3])))
        return est

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + ' ' + fornecedor.cnpj+ ' ' +
                            fornecedor.telefone+ ' ' + fornecedor.cpf)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('fornecedores.txt','r') as arq:
            cls.fornecedores = arq.readlines()
        cls.fornecedores = list(map(lambda x: x.replace('\n',''), cls.fornecedores))

        fornecd = []
        for i in cls.fornecedores:
            fornecd.append((Fornecedor(i[0], i[1], i[2], i[3])))
        return fornecd

class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'a') as arq:
            arq.writelines(pessoa.nome + ' ' + pessoa.cpf+ ' ' +
                            pessoa.email+ ' ' + pessoa.telefone+ ' ' +pessoa.endereco)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('pessoas.txt','r') as arq:
            cls.pessoas = arq.readlines()
        
        cls.pessoas = list(map(lambda x: x.replace('\n',''), cls.pessoas))

        clientes = []
        for i in cls.pessoas:
            clientes.append((Pessoa(i[0], i[1], i[2], i[3], i[4])))
        return clientes

class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.nome + ' ' + funcionario.cpf+ ' ' +funcionario.clt+ ' ' +
                        funcionario.email+ ' ' + funcionario.endereco+ ' ' + funcionario.telefone)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('funcionarios.txt','r') as arq:
            cls.funcionarios = arq.readlines()

        cls.funcionarios = list(map(lambda x: x.replace('\n',''), cls.funcionarios))

        funcionarios = []
        for i in cls.funcionarios:
            funcionarios.append((Funcionario(i[0], i[1], i[2], i[3], i[4], i[5])))
        return funcionarios

class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('vendas.txt', 'a') as arq:
            arq.writelines(venda.itensVendido.nomeProduto + ' ' + venda.itensVendido.preco+ ' ' +
                           venda.itensVendido.categoria +' '+str(venda.quantVendida)+ ' ' +
                           venda.data+''+ venda.vendedor+ ' '+ venda.comprador)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('vendas.txt','r') as arq:
            cls.vendas = arq.readlines()

        cls.vendas = list(map(lambda x: x.replace('\n',''), cls.vendas))

        vend = []
        for i in cls.vendas:
            vend.append(Venda(Produto(i[0], i[1], i[2], i[3], i[4], i[5])))
        return vend

