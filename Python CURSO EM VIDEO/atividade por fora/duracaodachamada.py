"""Converte a duração de uma chamada para horas, minutos e segundos."""

duracao_chamada = int(input('Duração da chamada em segundos: '))
limete_chamada = int(input('Limete gratuito em minutos: '))

h = duracao_chamada // 3600
m = (duracao_chamada % 3600) // 60
s = duracao_chamada % 60
minutos_total = duracao_chamada / 60 # minutos total
limete_chamada_segundos = limete_chamada * 60
segundos_excedido = 0
print(f'Duração convertida: {h:02d}h {m:02d}min {s:02d}s')
print(f'Limite: {limete_chamada} minutos')
if minutos_total > limete_chamada:
    segundos_excedido = duracao_chamada - limete_chamada_segundos
    print("Limete Ultrapassado!")
else:
    print("Limete não Ultrapassado!")
print(f'Tempo excedido: {segundos_excedido} segundos')
