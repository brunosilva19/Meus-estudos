nome = input('Digite algum: ')

print(f'Tipo primitivo:{type(nome)}')
print(f'Possui somente letras e números? {nome.isalnum()}')
print(f'Possui apenas letras? {nome.isalpha()}')
print(f'Possui apenas números? {nome.isnumeric()}')
print(f'Está em maiúsculas? {nome.isupper()}')
print(f'Está em minúsculas? {nome.islower()}')
