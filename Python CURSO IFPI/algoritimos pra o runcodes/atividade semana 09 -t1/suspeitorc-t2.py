perguntas = (
	"",
	"",
	"",
	"",
	"",
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
