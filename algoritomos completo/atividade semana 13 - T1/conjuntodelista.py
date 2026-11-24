lista_completa = []
lista_par = []
lista_impar = []

for c in range(20):
    num = int(input('Digite um número: '))
    lista_completa.append(num)
    lista_impar.append(num) if num % 2 == 0 else lista_impar.append(num)

print(f'lista completa: {lista_completa}')
print(f'lista PAR: {lista_par}')
print(f'lista IMPAR: {lista_impar}')