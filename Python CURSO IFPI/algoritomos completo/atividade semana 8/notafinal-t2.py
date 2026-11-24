def calcular_media_final(nota1, nota2, nota3, media_exercicios):
	return (nota1 + 2 * nota2 + 3 * nota3 + media_exercicios) / 7


def main():
	matricula = input("Número de matrícula: ")
	nota1 = float(input("Nota da prova 1: "))
	nota2 = float(input("Nota da prova 2: "))
	nota3 = float(input("Nota da prova 3: "))
	media_exercicios = float(input("Média dos exercícios: "))

	media_final = calcular_media_final(nota1, nota2, nota3, media_exercicios)
	if media_final >= 9.0:
		conceito = "A"
	elif media_final >= 7.5:
		conceito = "B"
	elif media_final >= 6.0:
		conceito = "C"
	elif media_final >= 4.0:
		conceito = "D"
	else:
		conceito = "E"
	situacao = "Aprovado" if conceito in ("A", "B", "C") else "Reprovado"

	print(f"Matrícula: {matricula}")
	print(f"Média final: {media_final:.2f}")
	print(f"Conceito: {conceito}")
	print(situacao)


if __name__ == "__main__":
	main()
