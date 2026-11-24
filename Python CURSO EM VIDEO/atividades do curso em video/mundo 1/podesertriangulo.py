print('-='*20)
print('Analisandor de triângulos')
print('-='*20)
a = float(input('Primerio segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMA triângulo!')
