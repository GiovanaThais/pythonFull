#funções
def soma_valores(n1, n2):
    print(n1 + n2)

soma_valores(2, 4)

#args (empacota valores em uma lista)
def func_lista(n1, n2, *args):
    print(f'n1= {n1} n2= {n2} args/resto={args}')

func_lista(1,2,4,5,6,7)

#kwargs (empacota valores em dicionario)
def func_nums(**kwargs):
    print(kwargs)
    x = kwargs.get('teste1')

func_nums(teste1= 1, teste2= 2, teste3= 3)

#modularizacao
