from re import T
from mercearia_model import Categoria, Estoque, Produto, Fornecedor, Pessoa, Funcionario, Venda
from mercearia_dao import DaoCategoria, DaoVenda, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario
from datetime import datetime


class ControllerCategoria:

    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print("Categoria cadastrada com sucesso")
        else:
            print("categoria ja existente, digite outra")

    def removercategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        categ = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(categ) <= 0:
            print('Acategoria não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso')

            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
    
    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        categ = list(filter(lambda x: x.categoria == categoriaAlterada, x))

        if len(categ) > 0:
            categ1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(categ1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x))
            else:
                print("categoria ja existe")

        else:
            print('categoria não existe')

        with open('categorias.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('categoria vazia!')
        else:
            for i in categorias:
                print(f'categoria: {i.categoria}')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        estoq = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) >0:
            if len(estoq) == 0:
                produto = Produto(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print("Produto cadastrado com sucesso")

            else:
                print('Produto ja existe em estoque')
        else:
            print("categoria inexistente")

    def removerProdutos(self, nome):
        x = DaoEstoque.ler()
        estoq = list(filter(lambda x: x.produto.nome == nome, x))
        if len(estoq) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break

        with open('estoque.txt', 'a') as arq:
            for i in x:
                arq.writelines(i.produto.nome + ' ' +i. produto.preco+ ' ' +
                                i.produto.categoria+ ' ' +str(i.quantidade))
                arq.writelines('\n')
    

    def alterarProdutos(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produto(novoNome, novoPreco, 
                        novaCategoria), novaQuantidade)if(x.produto.nome == nomeAlterar)else(x), x))
                    print('produto alterado com sucesso')
                else:
                    print('Produto ja cadastrado')

            else:
                print('produto informado nao existe')

            with open('estoque.txt', 'a') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + ' ' +i. produto.preco+ ' ' +
                                    i.produto.categoria+ ' ' +str(i.quantidade))
                    arq.writelines('\n')
        
        else:
            print('categoria informada nao existe')

    def mostrarProdutos(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('estoque vazio')
        else:
            for i in estoque:
                print("===== Produto =======")
                print(f'nome: {i.produto.nome}'
                      f'preço: {i.produto.preço}'
                      f'categoria: {i.produto.categoria}'
                      f'quantidade: {i.produto.quantidade}')


class ControllerVenda:

    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantddVendida):
        x = DaoEstoque.ler() #ver se tem no estoque
        temp = [] #variavel temporaria
        existe = False #representa que o produto nao existe
        quantidade = False #representa que o produto existe mas n tem quantdd suficiente

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto: #vericar se produto procurado por nome existe
                    existe = True
                    if int(i.quantidade) >= quantddVendida: #veridicar se quantidade é suficiente
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantddVendida)
                        vendido = Venda(Produto(i.produto.nomeProduto, i.produto.preco, i.produto.categoria),
                                                 vendedor, comprador, quantddVendida)
                        valorCompra = int(quantddVendida) * int(i.produto.preco)

                        DaoVenda.salvar(vendido)
            temp.append(Estoque[Produto(i.produto.nomeProduto, i.produto.preco, i.produto.categoria), i.quantidade])

        arq = open('estoque.txt', 'w')
        arq.write("")

        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i[0].nome+' '+ i[0].preco+' '+ i[0].categoria+' '+ str(i[1]))
                arq.writelines('\n')

            if existe == False:
                print('produto nao existe')
                return None
            elif not quantidade:
                print('venda realizada com sucesso')
                return valorCompra

    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.itensVendido.nomeProduto
            quantidade = i.quantddVendida
            tamanho = list(filter(lambda x: x['produo'] == nome, produtos))
            if len(tamanho)> 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade':x[quantidade] + int(quantidade)}
                if(x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})
            
        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)

        print('Esses sao os produtos mais vendidos')
        a = 1
        for i in ordenado:
            print(f'----- produto [{a}]-------')
            print(f"produto: {i['produto']}")
            print(f"quantidade: {i['quantidade']}")
            a+=1


class ControllerCliente:

    def cadastrarCliente(self):
        pass

    def alterarCliente(self, categoria):
        pass

    def removerCliente(self, categoria):
        pass

class ControllerFornecedor:

    def cadastrarFornecedor(self):
        pass

    def alterarFornecedor(self, categoria):
        pass

    def removerFornecedor(self, categoria):
        pass

class ControllerFuncionario:
    
    def cadastrarFuncionario(self):
        pass
    def alterarFuncionario(self):
        pass
    def removerFuncionario(self):
        pass
    def mostrarFuncionario(self):
        pass

