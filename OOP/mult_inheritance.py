#conceito de herança multipla 
class Animal:

    def andar(self):
        print('andar')
    
    def correr(self):
        print('correr')
    
    def pular(self):
        print('pular')

class Cachorro(Animal):

    def latir(self):
        print('latir')

class Felino(Animal):
    def felino(self):
        print(' felino') 

class Gato(Felino):

    def miar(self):
        print('miar')