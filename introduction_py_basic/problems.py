#exercicios de fixação -if else
#1- calculo de média
#2- aprovado/reprovado com if else 
nota1= float(input("digite nota 1: "))
nota2= float(input("digite nota 2: "))
nota3= float(input("digite nota 3: "))
media = (nota1+nota2+nota3)/3
if media >= 6:
    print("aprovado")
elif media < 6:
    print("reprovado")
#3- maior e menor numero
#for i in range(0,)
if nota1 > nota2 and nota1> nota3:
    print(f"o numero {nota1} é maior ")
elif nota1 < nota2 and nota2> nota3:
    print(f"o numero {nota2} é maior")

#4- positivo ou negativo 
if nota1 > 0:
    print(f"nota {nota1} é positiva")
else:
    print(f"nota {nota1} é negativa")
if nota2 > 0:
    print(f"nota {nota2} é positiva")
else: 
    print(f"nota {nota2} é negativa")
#5- masculino ou feminino
#6- temperatura 

#exercicios de fixação while 
i=0 
j=0
# while i <5 and j<10: 
#     print("olá")
#     #continue
#     i+=1
#     j+=2
#1- exercicio da tabuada
numero= float(input("digite um numero para gerar tabuada dele: "))

while i<10:
    mult = numero*i
    print(f"{numero} x {i} = {mult}")
    i+=1
#2- nota valida
while True:
    if media >=0 and media <=10:
        print(f'nota armazenada ')
        break
    print('nota invalida')

#3- login
user = 'giovana'
password = 'senha123'

while True:
    user_login = input('digite user: ')
    password_login = input('password: ')

    if user_login == user and password_login == password:
        print('logado')
        break
    else:
        print('user ou password invalid')
#4- numeros pares
num = input('digite um numero')
while i<= num:
    if i %2 ==0:
        print(i)
    i+=1

#exercicios de fixação for 
#1- tabuada com for 
for i in range(0, 11):
    mult = numero*i
    print(f"{numero} x {i} = {mult}")
#2- tabuada completa for
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
#3- numeros pares 
for i in range(0, 100, 2):
    # if i%2 == 0:
        print(i)

