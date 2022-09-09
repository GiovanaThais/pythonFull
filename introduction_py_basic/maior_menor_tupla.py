from random import sample

valores = tuple(sample(range(10), 5))

maior = max(valores)
menor = min(valores)

print(f'Os valores sorteados foram: {valores}')
print(f'maior valor sorteado foi:{maior}')
print(f'menor valor sorteado foi:{menor}')