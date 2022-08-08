from login_controller import ControllerCadastro, ControllerLogin


while True:
    print('---------- Menu ---------------------------------')
    menu = int(input('Digite 1 para cadastrar '
                 'Digite 2 para logar'
                 'Digite 3 para sair'))

    if menu == 1:
        name = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        password = input('Digite sua senha: ')

        result = ControllerCadastro.cadastrar(name, email, password)

        if result == 1:
            print('Cadastro realizado com sucesso')

        elif result == 2:
            print('Tamanho do nome invalido')
        elif result == 3:
            print('email maior que 200 caracteres')
        elif result == 4:
            print('tamanho da senha invalido')
        elif result == 5:
            print('email ja cadastrado')
        elif result == 6:
            print('erro interno do sistema')
        

    elif menu == 2:
        email = int('Digite seu email: ')
        password = int('Digite seu password: ')
        
        result = ControllerLogin.login(email, password)

        if not result:
            print('email ou senha invalidos')
        else:
            print(result)
    
    else:
        break
