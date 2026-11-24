duraca = float(input('Qual a duração do vídeo em segundos: '))

hora = duraca // 3600
#minuto = (duraca - (hora * 3600)) // 60
minuto = ( duraca % 3600 ) // 60
#segundos = duraca - (hora * 3600 + minuto * 60)
segundos = duraca % 60

print(f'Duração convertida: {hora:.0f}h {minuto:.0f}min {segundos:.0f}s')
