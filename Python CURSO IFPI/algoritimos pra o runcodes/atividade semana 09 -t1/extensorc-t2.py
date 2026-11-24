numero = int(input(''))

nomes = ["zero", "uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
partes = []

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

if centenas:
	nome = "uma" if centenas == 1 else nomes[centenas]
	partes.append(f"{nome} {'centena' if centenas == 1 else 'centenas'}")

if dezenas:
	partes.append(f"{nomes[dezenas]} {'dezena' if dezenas == 1 else 'dezenas'}")

if unidades:
	partes.append(f"{nomes[unidades]} {'unidade' if unidades == 1 else 'unidades'}")

if not partes:
	partes.append("zero unidades")

if len(partes) == 1:
	resultado = partes[0]
elif len(partes) == 2:
	resultado = " e ".join(partes)
else:
	resultado = f"{partes[0]}, {partes[1]} e {partes[2]}"

print(resultado + ".")
