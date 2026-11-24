"""Relatório de desempenho escolar"""
# entrada de dados
alunos = int(input('Digite a quantidade de alunos: '))
lista_aluno = []
lista_nota = []
lista_media = []
lista_aprovacao = []
count_aprovados = 0
count_reprovados = 0
count_recuperaca = 0
count_destaque = 0
media_geral = 0
maior_media = 0
nome_maior = ''
menor_media = 0
nome_menor = ''
for c in range(0, alunos):
    nome_aluno = input('Digite o nome do aluno: ').title().strip()
    lista_aluno.append(nome_aluno)

    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lista_nota.append([nota1, nota2])
    # calculador para os alunos
    lista_media.append((lista_nota[c][0]+lista_nota[c][1]) / 2)
    media_geral += lista_media[c]
    if c == 0:
        maior_media = lista_media[c]
        menor_media = lista_media[c]
        nome_maior = lista_aluno[c]
        nome_menor = lista_aluno[c]

    if lista_media[c] > maior_media:
        maior_media = lista_media[c]
        nome_maior = lista_aluno[c]

    elif lista_media[c] < menor_media:
        menor_media = lista_media[c]
        nome_menor = lista_aluno[c]

    # condições
    if lista_media[c] >= 9:
        lista_aprovacao.append('Aprovado(a) com destaque!')
        count_destaque += 1
    elif lista_media[c] >= 7:
        lista_aprovacao.append('Aprovado(a)!')
        count_aprovados += 1
    elif lista_media[c] >= 5:
        lista_aprovacao.append('Recuperação!')
        count_recuperaca += 1
    else:
        lista_aprovacao.append('Reprovado(a)!')
        count_reprovados += 1
media_total = media_geral / alunos
print(f'{" Relatório ":=^40}')
for a in range(0, alunos):
    print(
        f'{lista_aluno[a]} — Média {lista_media[a]:.2f} — {lista_aprovacao[a]}')
print(f'Aprovados: {count_aprovados + count_destaque}')
print(f'Em recuperação: {count_recuperaca}')
print(f'Reprovados: {count_reprovados}')
print(f'Alunos com destaque: {count_destaque}')
print(f'Média geral da turma: {media_total:.2f}')
print(f'Maior média: {nome_maior} - {maior_media:.2f}')
print(f'Menor média: {nome_menor} - {menor_media:.2f}')
