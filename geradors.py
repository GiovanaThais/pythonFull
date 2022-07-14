#geradores gastam muito menos memoria para executar functions simples
# from pympler.asizeof import asizesof


def dobro():
    yield 1 
    yield 2
    yield 3
x = dobro()

print(next(x))
#exemplo 
def dobro1(lista):
    for i in lista:
        yield i*2

def dobro2(lista):
    lista2 = []
    for i in lista:
        lista2.append(i)
    return lista2

y= dobro2(range(0, 20))
z= dobro1(range(0, 20))

# print(asizesof(y))
# print(asizesof(z))