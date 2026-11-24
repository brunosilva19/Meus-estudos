"""CONSUMO DE ENERGIA DE UM APARELHO """

pontencia = float(input('Qual a pontência do aparelho: '))
uso_por_dia = float(input('Quantas horas de uso diário: '))
quantidade_de_dias = int(input('Quantidade de dias de uso: '))
preco_do_kwh = float(input('Proço do KWh: R$'))

consumo = (pontencia * uso_por_dia * quantidade_de_dias)/1000
valor_aser_pago = consumo * preco_do_kwh 
print('='*60)
print(f'O consumo estimado é de: {consumo:.2f} KWh')
print(f'O valor a ser pago por {consumo:.2f} KWh é de: R$ {valor_aser_pago:.2f}')
print('='*60)
