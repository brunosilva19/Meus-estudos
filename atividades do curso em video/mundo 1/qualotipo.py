nome = input('Digite algum:')

print(f'O tipo primitivo desse valor é {type(nome)}')
print(f'so tem espaços? {nome.isspace()}')
print(f'É um número? {nome.isnumeric()}')
print(f'É alfabetico? {nome.isalpha()}')
print(f'Está em maiúsculo? {nome.isupper()}')
print(f'Está em minúsculo? {nome.islower()}')
print(f'Está capitalizada? {nome.istitle()}')