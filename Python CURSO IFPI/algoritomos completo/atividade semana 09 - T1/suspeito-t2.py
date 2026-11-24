perguntas = (
	"Telefonou para a vítima? (S/N): ",
	"Esteve no local do crime? (S/N): ",
	"Mora perto da vítima? (S/N): ",
	"Devia para a vítima? (S/N): ",
	"Já trabalhou com a vítima? (S/N): ",
)

respostas_sim = 0
for pergunta in perguntas:
	resposta = input(pergunta).strip().upper()
	if resposta == "S":
		respostas_sim += 1

classificacao = (
	"Inocente",
	"Inocente",
	"Suspeito",
	"Cúmplice",
	"Cúmplice",
	"Assassino",
)[respostas_sim]

print(classificacao)
