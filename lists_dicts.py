nomes=[]
idades=[2,3,5,6,7,8,12,15]
while True:
    nome= input("digite um nomeou -1 para sair: ")
    if nome == "-1":
        break
    nomes.append(nome) #insere no final
    nomes.pop() #remove o ultimo item da lista
    nomes.pop(2)#remove pelo index
    nomes.insert(0, "julia") #insert em qualquer posição da lista
    nomes.remove("julia") #remove pelo valor do index
    print(nomes.index('julia')) #verificar em qual index esta o obj
    nomes.pop(nomes.index('julia')) #remove pelo index
print(nomes)
print(sorted(nomes)) #ordenando lista
iterador = list(enumerate(nomes))

idades_pares = [] 
for i in idades:
    if i %2 == 0:
        idades_pares.append(i)

print(idades_pares)
#1-exercicio listas
x = [int(input('digite um numero')) for i in range(0, 10)]

soma = 0
for i in x:
    soma += 1
print(soma)
print(sum(x))

y= []
for i in range(0, 10):
    y.append(i) #forma de fazer contador sem list comprehension
#2-list comprehension
z= [i for i in range(0, 10)]
lista = [2,4,5,6,7,8]
mult = [i*2 for i in lista] #multiplica cada item da lista acima e armazena na lista mult
#3-exercicio list comprehension
#percorrer uma matriz com list comprehension
x= [[input() for j in range(0, 2)] for i in range(0, 2)]
#add valores a lista quando valor de i for maior que 4 
y=[]
for i in range(0, 10):
    if i> 4:
        y.append(i) 
#com list comprehension:
x= [i for i in range(0, 10) if i>4]

#1-exercicio dictionary
pessoas = [{'nome':'Caio','idade':24},
            {'nome':'Julia','idade':22}]
for pessoa in pessoas:
    print(pessoa['nome'])

#2-exercicio dictionary
cadastro = []
while True:
    menu= int(input('digite 1-cadastrar 2-sair'))
    if menu ==2:
        break
    pessoa = {'nome':str(input('digite um nome: ')), 
            'idade':int(input('digite a idade: ')),
             'altura':float(input('digite a altura:'))}
    cadastro.append(pessoa)

    cadastro.update({'cep':int(input('digite o cep: '))})
    print(cadastro.items())
    print(cadastro.keys())

#conjuntos
x= {1,1,3,4,5} #conjuntos nao contam numeros repetidos(descartam)
y= {2,2, 6, 8, 5}
print(x.union(y)) #uniao de conjuntos
print(x.intersection(y)) #intersection de conjuntos
print(x.difference(y))
print(x.symmetric_difference(y)) #união sem intersecção 