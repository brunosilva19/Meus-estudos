def calcular_peso_ideal(altura, sexo):
	if sexo == 1:
		return (72.7 * altura) - 58
	elif sexo == 2:
		return (62.1 * altura) - 44.7
	return None


def mostrar_resultado(peso_ideal):
	if peso_ideal is None:
		print("Sexo inválido. Digite 1 para homens ou 2 para mulheres.")
	else:
		print(f"Peso ideal: {peso_ideal:.2f} kg")

def main():
	altura = float(input("Digite a altura em metros: "))
	sexo = int(input("Digite 1 para homens ou 2 para mulheres: "))
	peso_ideal = calcular_peso_ideal(altura, sexo)
	mostrar_resultado(peso_ideal)


if __name__ == "__main__":
	main()
