"""Programa para analisar propriedades de um nome informado pelo usuário."""

nome: str = input('Digite um nome de Usuário: ')

print(f'O tipo primitivo: {type(nome)}')
print(f'Possui somente letras e números? {nome.isalnum()}')
print(f'Possui apenas letras? {nome.isalpha()}')
print(f'Possui apenas números? {nome.isnumeric()}')
print(f'Está tortalmente em minúsculas? {nome.islower()}')
