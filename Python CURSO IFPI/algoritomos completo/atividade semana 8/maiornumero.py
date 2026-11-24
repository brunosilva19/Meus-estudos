maior = 0
menor = 0
for c in range(1,6):
    numero = int(input(f'Digite o {c}º número: '))
    if c == 1:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')