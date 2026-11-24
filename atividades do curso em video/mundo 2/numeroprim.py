""""numero primo"""
divisores = 0
numero = int(input('Digite um número: '))
for c in range(1, numero+1):
    if numero % c == 0:
        print(f'\033[33m{c}\033[m', end=' ')
        divisores += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO número {numero} foi divisível {divisores} vezes.')
if divisores == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
