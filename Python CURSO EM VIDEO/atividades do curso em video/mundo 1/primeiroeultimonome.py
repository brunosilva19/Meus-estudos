"""Exibe o primeiro e o último nome informados pelo usuário."""

nome_completo = input('Digite o seu nome completo: ').strip()
nome_separado = nome_completo.split()
print(f'Seu primeiro nome é: {nome_separado[0].capitalize()}')
print(f'Seu último nome é: {nome_separado[-1].capitalize()}')
