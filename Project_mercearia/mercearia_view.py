import mercearia_controller
import os.path


def criaArquivo(*args):
    for i in args:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write("")

criaArquivo("categorias.txt", "clientes.txt", "estoque.txt",
             "fornecedores.txt", "funcionarios.txt", "vendas.txt")

if __name__ == "__main__":
    while True:
        menu = int(input("Digite 1 para acessar Categorias "+ " "+
                        "Digite 2 para acessar Estoque"+" "+
                        "Digite 3 para acessar Fornecedor"+" "+
                        "Digite 4 para acessar Cliente"+" "+
                        "Digite 5 para acessar Funcionarios"+" "+
                        "Digite 6 para acessar Vendas"+" "+
                        "Digite 7 para sair"))
        
        if menu == 1:
            categoria = mercearia_controller.ControllerCategoria()

            while True:
                menu1 = int(input("Digite 1 para cadastrar categoria"+" "+
                                  "Digite 2 para remover categoria"+" "+
                                  "Digite 3 para alterar categoria"+" "+
                                  "Digite 4 para mostrar categoria"+" "+
                                  "Digite 5 para sair"))
                if menu1 == 1:
                    categorias = input("Digite a categoria que deseja cadastrar")
                    categoria.cadastraCategoria(categorias)
                elif menu1 == 2:
                    categorias = input("Digite a categoria que deseja remover")
                    categoria.removercategoria(categorias)
                elif menu1 == 3:
                    categorias = input("Digite a categoria que deseja alterar")
                    novaCategoria = input("Digite a nova categoria")
                    categoria.alterarCategoria(categorias, novaCategoria)
                elif menu1 == 4:
                    categoria.mostrarCategoria()
                else:
                    break

        if menu == 2:
            estoque = mercearia_controller.ControllerEstoque()
            while True:
                menu2 = int(input("Digite 1 para cadastrar produto"+" "+
                                  "Digite 2 para remover produto"+" "+
                                  "Digite 3 para alterar produto"+" "+
                                  "Digite 4 para mostrar estoque"+" "+
                                  "Digite 5 para sair"))
                
                if menu2 == 1:
                    nomeProduto = input("Digite o produto que deseja cadastrar: ")
                    preco = int(input("Digite o preço do produto: "))
                    estoque.cadastrarProduto(nomeProduto, preco)
                elif menu2 == 2:
                    nomeProduto = input("Digite o nome do produto que deseja remover")
                    estoque.removerProdutos(nomeProduto)
                elif menu2 == 3:
                    nomeProduto = input("Digite o produto que deseja alterar")
                    novoProduto = input("Digite o novo produto")
                    estoque.alterarProdutos(nomeProduto, novoProduto)
                elif menu2 == 4:
                    estoque.mostrarProdutos()
                else:
                    break
                
        if menu == 3:
            fornecedor = mercearia_controller.ControllerFornecedor()
        
        if menu == 4:
            cliente = mercearia_controller.ControllerCliente()

        if menu == 5:
            funcionario = mercearia_controller.ControllerFuncionario()
        
        if menu == 6:
            vendas = mercearia_controller.ControllerVenda()
            vendas.relatorioProdutos()

        if menu == 7:
            break
