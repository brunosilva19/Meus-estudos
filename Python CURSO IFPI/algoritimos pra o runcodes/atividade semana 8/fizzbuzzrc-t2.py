def e_divisivel(numero, divisor):
	return numero % divisor == 0


def verificar_numero(numero):
	if e_divisivel(numero, 3) and e_divisivel(numero, 5):
		return "FIZZBUZZ"
	elif e_divisivel(numero, 3):
		return "FIZZ"
	elif e_divisivel(numero, 5):
		return "BUZZ"
	else:
		return numero


def main():
	numero = int(input(""))
	print(verificar_numero(numero))


if __name__ == "__main__":
	main()
