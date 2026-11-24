def e_divisivel(numero, divisor):
	return numero % divisor == 0


def main():
	numero = int(input("Digite um número inteiro: "))
	if e_divisivel(numero, 3) and e_divisivel(numero, 5):
		print("FIZZBUZZ")
	elif e_divisivel(numero, 3):
		print("FIZZ")
	elif e_divisivel(numero, 5):
		print("BUZZ")
	else:
		print(numero)


if __name__ == "__main__":
	main()
