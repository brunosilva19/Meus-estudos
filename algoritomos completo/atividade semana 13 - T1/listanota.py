n = int(input('valor: '))
valores = []
for i in range(n):
    valor = float(input(f'valor {i + 1}: '))
    valores.append(valor)
print([f'{valor:.4f}' for valor in valores[::-1]])

notas = []
for i in range(n):
    nota = float(input(f'nota {i + 1}: '))
    notas.append(nota)
print('Notas:', [f'{nota:.1f}' for nota in notas])
if n == 0:
    print('SEM NOTAS')
else:
    print(f'Média: {sum(notas) / n:.1f}')

consoantes = []
vogais = 'aeiou'
quantidade_vogais = 0
for i in range(n):
    letra = input(f'letra {i + 1}: ')[0]
    if letra.lower() in vogais:
        quantidade_vogais += 1
    else:
        consoantes.append(letra)
        
print('Quantidade de vogais:', quantidade_vogais)
print('Consoantes:', consoantes)