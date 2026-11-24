valor_compra = float(input("Digite o valor da compra: R$ "))

for parcelas in range(1, 25):
	valor_prestacao = valor_compra / parcelas
	print(f"{parcelas}x de R$ {valor_prestacao:.2f}")
