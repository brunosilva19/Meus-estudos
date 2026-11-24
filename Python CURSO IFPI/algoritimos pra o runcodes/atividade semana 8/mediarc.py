media = 0
numeros = []
maiores_que_media = []

for _ in range(5):
    numero = int(input(''))
    numeros.append(numero)
    media += numero

media = media / len(numeros)
print(f'{media:2.1f}')

for numero in numeros:
    if numero > media:
        maiores_que_media.append(f'{numero:2.0f}')
for c in maiores_que_media:
    print(c)
