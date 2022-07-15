#conceito de herança
class Pessoa:
    
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    def falar(self):
        print('falando')

    def andar(self):
        print('andando')

    
class Cliente(Pessoa): #cliente herda tudo de cliente ( endidade filho tem metodos da classe pai)    
    
    def __init__(self, id_cliente, nome, cpf):
        super().__init__(nome, cpf)
        self.id_cliente = id_cliente
    
    def comprar(self):
        print('comprando')

    #sobrepondo metodos da classe pai
    def andar(self):
        super().andar() #chamando classe pai para nao ter sobreposição
        print('correndo')

class Vendedor(Pessoa): #vendedor possui atributos de pessoa
    
    def vender(self):
        print('vendendo')

c1 = Cliente()
c1.andar()
c1.falar()
c1 = Cliente(2, 'Giovana', '12332211')
print(c1.nome)
print(c1.cpf)