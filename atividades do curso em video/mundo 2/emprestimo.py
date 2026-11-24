"""Programa para aprovar um emprestimo"""

# entrada de dados
valor_da_casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual o seu salário: R$ '))
anos = int(input('Em quantos anos você quer pagar a casa: '))

# calculos para o programa

valor_da_parcela = valor_da_casa / (anos * 12)
porcentagem_do_salario = salario * 0.3

# saida para o usuario

print(f'Para pagar uma casa de R$ {valor_da_casa:.2f} em {anos} anos a prestação será de R$ {valor_da_parcela:.2f}.')

# condição para aprovar a compra

if valor_da_parcela > porcentagem_do_salario:
    print('Empréstimo: \033[31mNEGADO!\033[m')
else:
    print('Empréstimo: \033[32mCONCEDIDO!\033[m')
