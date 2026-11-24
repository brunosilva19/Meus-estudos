s = int(input('Digite uma quantidade de tempo sem segundos: '))

minutos = s // 60
segundos = s % 60

print(f'{s} segundos corresponde a {minutos} M e {segundos} S')