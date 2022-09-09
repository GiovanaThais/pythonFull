from datetime import datetime

dataNasc = int(input("digite seu ano de nascimento: "))

dataHoje = datetime.today().year 
dataVoto = dataHoje- dataNasc

if dataVoto >= 18:
    print(f"voto obrigatorio: {dataVoto} anos de idade")
if dataVoto == 17:
    print(f"voto opcional {dataVoto} anos de idade")
if dataVoto <16:
    print(f"voto negado {dataVoto} anos de idade")
