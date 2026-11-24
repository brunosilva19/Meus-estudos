n = int(input(''))

valores = []
for i in range(n):
    valor = float(input(f''))
    valores.append(valor)
print(valores[::-1])

notas = []
for i in range(n):
    nota = float(input(f''))
    notas.append(nota)
print(notas[:])
if n == 0:
    print('SEM NOTAS')
else:
    print(f'{sum(notas) / n:.1f}')

consoantes = []
vogais = 'aeiou'
quantidade_vogais = 0
for i in range(n):
    letra = input()[0]
    if letra.lower() in vogais:
        quantidade_vogais += 1
    else:
        consoantes.append(letra)
print(quantidade_vogais)
print(consoantes)