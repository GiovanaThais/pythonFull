#tratamento de exceções
try:
    n1= int(input('digite um numero '))
    n2= int(input('digite outro numero '))
except ValueError:
    print('digite um numero inteiro')
except ZeroDivisionError:
    print('sistema não comporta zeros na divisao')

try:
    print(n1/n2)
except:
    print('erro na divisao')
finally:
    print('Finalizado!')

#raise e assert
def soma_numeros(n1, n2):
    if n1 < 0 or n2 < 0:
        #raise ValueError('n1 e n2 nao podem ser negativos')
        assert n1 < 0 or n2 < 0 ,"não aceita numeros negativos"
    return n1 + n2

print(soma_numeros(2, -2))