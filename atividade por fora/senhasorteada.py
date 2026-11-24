"""Sorteia uma senha entre as pessoas informadas."""

from random import randint

pessoas = int(input('Quantidade de pessoas: '))
senha = int(input('Qual a sua senha: '))
senha_sorteada = randint(1, pessoas)
print(f'Senha sorteada: {senha_sorteada}')
if senha_sorteada == senha:
    print('Sua senha foi selecionada!')
else:
    print('A sua senha não foi selecionada.')
