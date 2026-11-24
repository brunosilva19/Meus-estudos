valor_inicial = float(input('Qual o valor de investimento: R$ '))
tax_juros = float(input('Qual a taxa de juros: '))
quant_meses = int(input('Quantidade de meses: '))

montante = valor_inicial * pow(1 + tax_juros / 100, quant_meses)

print(f'O valor final foi de : R$ {montante:.2f}')
print(f'Total ganho em juros: R$ {montante - valor_inicial:.2f}')
