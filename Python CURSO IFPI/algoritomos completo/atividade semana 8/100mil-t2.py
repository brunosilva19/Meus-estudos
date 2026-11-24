def soma_digitos(numero):
	if numero < 0 or numero > 100000:
		return -1

	soma = 0
	for digito in str(numero):
		soma += int(digito)

	return soma


def main():
	numero = int(input("Digite um número inteiro: "))
	print(soma_digitos(numero))


if __name__ == "__main__":
	main()
