from controller import PessoaController


while True:
    decisao = int(input('Digite 1- salvar, 2-verificar 3-sair : '))
    if decisao == 3:
        break
    if decisao == 1:
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))
        cpf = int(input('Digite seu cpf: '))

        if PessoaController.cadastrar(nome, idade, cpf):
            print('user cadastrado com sucesso!')
        else:
            print('digite valores validos')