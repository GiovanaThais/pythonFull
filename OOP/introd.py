class Pessoas:
    possui_olhos = True
    possui_boca = True #atributos de classe

    def __init__(self, name, idade, cpf):
        self.name = name #variavel/atributo de instancia
        self.idade = idade
        self.cpf = cpf

    def retorna_nome(self):
        return self.name

    def logar_sistema(self):
        print(f'{self.retorna_nome}logando no sistema')

    #metodo de classe possui um decorador
    @classmethod
    def andar(cls, velocidade):
        #cls referencia a classe chamada pelo classmethod
        print('andando na velocidade {velocidade} m/s')
        #atravez do cls é possivel alterar atributos de classe
        cls.possui_boca = False

    #metodos estaticos acompanham um decorador
    @staticmethod
    def eh_adulto(idade):
        if idade > 18:
            return True
        return False
    #metodos estaticos apenas acessam atributos da classe mas não podem modificar
    #metodos estaticos não nessecitam de cls ou self

p1 = Pessoas('Maria', 22, '21232444')
p2 = Pessoas('Julia', 33, '234455566')

print(p1.name)
print(p2.name)
Pessoas.andar(12)
print(p1.logar_sistema())