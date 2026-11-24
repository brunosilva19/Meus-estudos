lista_completa = []
lista_par = []
lista_impar = []

for c in range(20):
    num = int(input(''))
    lista_completa.append(num)
    lista_par.append(num) if num % 2 == 0 else lista_impar.append(num)

print(f'{lista_completa}')
print(f'{lista_par}')
print(f'{lista_impar}')