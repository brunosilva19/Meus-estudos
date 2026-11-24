num = int(input('Quantos termos você quer mostrar: '))
primeiro_termo = 0
segundo_termo = 1
print(f'{primeiro_termo} ➝  {segundo_termo}', end=' ')
coun = 3
while coun <= num:
    t3 = primeiro_termo + segundo_termo
    print(f' ➝  {t3}', end=' ')
    primeiro_termo = segundo_termo
    segundo_termo = t3
    coun += 1
print(' ➝  FIM')