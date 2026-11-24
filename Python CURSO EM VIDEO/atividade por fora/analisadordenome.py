nome = input('Digite seu nome completo: ').strip().upper()
separado = nome.split()
print(f'Maiúscula: {nome.upper()}')
print(f'Minúscula: {nome.lower()}')
print(f'Quantidade de letras: {len("".join(separado))}')
print(f'Primeiro nome é: {separado[0].capitalize()}')
print(f'Último nome: {separado[-1].capitalize()}')
if 'SILVA' in separado:
    n = 'sim'
else:
    n = 'Não'
print(f'Possui Silva no nome: {n} ')
