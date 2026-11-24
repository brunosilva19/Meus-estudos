from math import trunc

num = float(input('Digite um valor: '))

print(f'O valor digitado foi {num} e sua parte inteira é {trunc(num)}' ' = aqui foi usando o modulo TRUNC')
print(f'O valor digitado foi {num} e sua parte inteira é {num//1:.0f}' ' = aqui foi usando a divisão inteira //')
print(f'O valor digitado foi {num} e sua parte inteira é {int(num)}' ' = aqui foi usado a função int()')