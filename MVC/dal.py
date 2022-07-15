from model import Pessoa


class PessoaDal:

    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'w') as arq:
            arq.write(pessoa.nome +" "+str(pessoa.idade)+" "+ pessoa.cpf)
    
    @classmethod
    def ler(cls):
        # with open('pessoas.txt', 'r') as arq:
        #     arq.read()
        
        nome = 'Maria'
        idade = 19
        cpf = "929222" 
        return Pessoa(nome, idade, cpf)

p1 = Pessoa('Maria', 19, '23423211')
