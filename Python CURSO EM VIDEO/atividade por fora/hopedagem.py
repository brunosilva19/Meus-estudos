idade_total = 0
mais_velha_nome = ''
mais_velha_idade = 0
mulher_menos_25 = 0
homem_maior_40 = 0
total_gasto = 0
for pessoas in range(1, 6):
    nome = input(f"Nome da pessoa {pessoas}: ").strip().capitalize()
    idade = int(input(f"Idade da pessoa {pessoas}: "))
    idade_total += idade
    sexo = input(f"Sexo (M/F) da pessoa {pessoas}: ").strip().upper()
    if sexo == 'F' and idade < 25:
        mulher_menos_25 += 1
    if sexo == 'M' and idade > 40:
        homem_maior_40 += 1
    valor_hospedagem = float(input(f"Valor gasto na hospedagem da pessoa {pessoas}: R$ "))
    total_gasto += valor_hospedagem
    print('='*40)
    if pessoas == 1:
        mais_velha_idade = idade
        mais_velha_nome = nome
    if idade > mais_velha_idade:
        mais_velha_idade = idade
        mais_velha_nome = nome
print(f'{'RELATÓRIO':=^40}')
print(f'Média de idade: {idade_total/5:.2f}')
print(f'Pessoa mais velha: {mais_velha_nome} - {mais_velha_idade}')
print(f'Mulheres com menos de 25 anos: {mulher_menos_25}')
print(f'Homens com mais de 40 anos: {homem_maior_40}')
print(f'Total dos gastos: R$ {total_gasto:.2f}')
print(f'Média dos gastos: R$ {total_gasto/5:.2f}')