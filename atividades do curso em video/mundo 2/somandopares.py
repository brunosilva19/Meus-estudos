"""soma somente dos numeros pares"""
soma = 0
quantidade = 0
for c in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
        quantidade += 1
print(f'Dos 6 números informados, {quantidade} são pares e a sua soma é de {soma}')
