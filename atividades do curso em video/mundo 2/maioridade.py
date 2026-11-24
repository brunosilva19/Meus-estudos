"""esse programa vai ler quantas pessoas ja sao maior de idade"""
from datetime import date
atual = date.today().year
maior_idade = 0
menor_idade = 0
for c in range(1,8):
    ano = int(input(f'Digite o {c}º ano de nascimento: '))
    idade = atual - ano
    if idade < 18:
        menor_idade += 1
    else:
        maior_idade += 1
print(f'{menor_idade} pessoas ainda não são maiores de idade.')
print(f'{maior_idade} pessoas são maiores de idade.')
