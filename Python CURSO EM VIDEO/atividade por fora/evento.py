hora_inicial = int(input('Horas de início: '))
minutos_inicial = int(input('Minutos de início: '))
quantidade_de_atividades = int(input('Quantidade de atividades: '))
print(f'{'ATIVIDADES':=^40}')
minutos_totais = 0
maior_tempo = 0
menor_tempo = 0
for atividades in range(quantidade_de_atividades):
    duracao = int(input(f'Duração da atividade {atividades + 1}: '))
    minutos_totais += duracao
    if atividades == 0:
        maior_tempo = duracao
        menor_tempo = duracao
    if duracao > maior_tempo:
        maior_tempo = duracao
    if duracao < menor_tempo:
        menor_tempo = duracao
print(f'{'='*40}')
#CALCULOS PARA O PROGRAMA
horas = minutos_totais // 60
minuto = minutos_totais % 60
total_minutos_geral = (hora_inicial * 60) + minutos_inicial + minutos_totais
hora_final = (total_minutos_geral // 60) % 24
minuto_final = total_minutos_geral % 60
dias = (total_minutos_geral // 60) // 24
print(f'Duração total: {horas:02d}h {minuto:02d}min')
print(f'Média por atividade: {minutos_totais/quantidade_de_atividades:.2f} minutos')
print(f'Maior duração: {maior_tempo} minutos')
print(f'Menor duração: {menor_tempo} minutos')
print(f'Horário de encerramento: {hora_final:02d}:{minuto_final:02d}')
print(f'Mudanças de dia: {dias}')
if dias == 0:
    print('O evento terminará no mesmo dia!')
elif dias == 1:
    print('O evento terminará no dia seguinte!')
else:
    print(f'O evento terminará {dias} dias após o dia de início!')