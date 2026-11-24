data = input("Digite a data no formato DDMMAAAA: ")

if len(data) != 8 or not data.isdigit():
	print("Data inválida")
else:
	dia = int(data[0:2])
	mes = int(data[2:4])
	ano = int(data[4:8])

	if ano > 0 and 1 <= mes <= 12:
		if mes == 2:
			if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
				dias_no_mes = 29
			else:
				dias_no_mes = 28
		elif mes in (4, 6, 9, 11):
			dias_no_mes = 30
		else:
			dias_no_mes = 31

		if 1 <= dia <= dias_no_mes:
			print(True)
		else:
			print(False)
	else:
		print(False)
