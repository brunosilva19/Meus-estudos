"""Analisador completo"""
# entrada de dados
idade_total = 0
nome_homen = ''
idade_homem = 0
cont = 0
for c in range(1, 5):
    print('-='*30)
    nome = input(f'Digite o nome da {c}º pessoa: ').strip().title()
    idade = int(input('Digite a idade: ').strip())
    sex = input('Qual a sua sexualidade [M/F]: ').strip().upper()
    idade_total += idade
    if sex == 'M' and idade > idade_homem:
        nome_homen = nome
        idade_homem = idade
    if sex == 'F':
        if idade < 20:
            cont += 1
idade_media = idade_total / c
print(f'A idade média do grupo é: {idade_media:.1f} anos.')
print(f'O homem mais velho tem {idade_homem} anos e se chama {nome_homen}.')
print(f'Ao todo temos {cont} mulher(es) com menos de 20 anos.')
