def notas(num, sit=False):
    """
    -> Função que mostra uma situação geral de notas dos alunos:
    :param qtdnt: quantidade de notas inseridas;
    :param maiorn: maior nota inserida;
    :param menorn: menor nota inserida;
    :param median: média das notas inseridas;
    :param sit: situação dos alunos;
    :return: retorna todos os parametros acima dentro ou não de uma situação
    """
    dictnt = dict()
    dictnt['total'] = len(num)
    dictnt['maior'] = max(num)
    dictnt['menor'] = min(num)
    dictnt['média'] = sum(num)/len(num)
    print(type(num))
    if sit:
        if dictnt['média'] >= 9:
            dictnt['sit'] = 'ÓTIMA'
        elif dictnt['média'] >= 7:
            dictnt['sit'] = 'BOA'
        elif dictnt['média'] >= 5:
            dictnt['sit'] = 'REGULAR'
        else:
            dictnt['sit'] = 'RUIM'
    return dictnt


#Programa Principal
nota = list()
cont = 1
print('Digite as notas dos alunos!')
while True:
    resp = float(input(f'Digite a nota do {cont}º aluno: '))
    nota.append(resp)
    d = input('Deseja continuar [S/N]? ')
    cont+=1
    if d in 'nN':
        break
print(notas(nota, sit=True))












# def analisando_notas(*nota):
#     notas = dict()

#     notas['total'] =  len(nota)
#     notas['maior'] = max(nota)
#     notas['menor'] = min(nota)
#     notas['media'] = sum(nota)/len(nota)

# dicionario = analisando_notas(5.5,2.5,7.8, 4.5)
# print(dicionario)
