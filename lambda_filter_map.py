#lambda é uma função sem def mais direta
x = lambda nome,idade : print(nome , idade)
x('Giovana', 22)

#lambda com *args empacotando em tupla
z = lambda *cep: print(cep)
z ('12344','1111','9292')

#filter 
x = [12, 21, 33, 44, 52, 14]
x1 = [{'nome':'josé', 'idade':12}, {'nome':'maria', 'idade':22}]
x = list(filter(lambda x: x <18, x))
x1 = list(filter(lambda x: x['idade']> 20, x1))

print(x)
print(x1)