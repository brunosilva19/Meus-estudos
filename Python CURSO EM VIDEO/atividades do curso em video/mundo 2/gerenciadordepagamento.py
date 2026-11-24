"""Programa para gerenciar a forma de pagamento de estabececimento"""
print(f'{' LOJAS BS SHOP ':=^60}')
valor_compras = float(input('Preço das compras: R$ '))
ops = int(input("""FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção: """))
if ops == 1:
    valor_final = valor_compras - valor_compras * 0.1
    print(f"Para compra à vista dinheiro/cheque temos 10% de desconto.\nSuas compras de R$ {valor_compras:.2f} com esse desconto vai ficar de R$ {valor_final:.2f}")
elif ops == 2:
    valor_final = valor_compras - valor_compras * 0.05
    print(f"Para compra à vista no cartão temos 5% de desconto.\nSuas compras de R$ {valor_compras:.2f} com esse desconto vai ficar de R$ {valor_final:.2f}")
elif ops == 3:
    valor_final = valor_compras / 2
    print(f"o valor de suas compras é de R$ {valor_compras:.2f}\nA parcela vai ficar de R$ {valor_final:.2f}")
elif ops == 4:
    numero_de_parcela = int(input('Quantas parcelas: '))
    valor_final = valor_compras + valor_compras * 0.2
    valor_da_parcela = valor_final / numero_de_parcela
    print(f"Para compra de 3x ou mais vezes, tem 20% de juros.\nSuas compras de R$ {valor_compras:.2f} vai passar a custar R$ {valor_final:.2f} com juros.")
    print(f'Com parcelas de R$ {valor_da_parcela:.2f}')
else:
    print('Opção invalida, tente novamente')
