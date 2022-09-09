from calendar import c


print('='*20)
print('{:^20}'.format('Banco GTGC'))
print('='*20)

valor = int(input("digite o valor que deseja sacar: "))
total = valor 
cedula = 50
totalCedula =0

while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1

    else:
        print(f'total de {totalCedula} cedulas de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break
