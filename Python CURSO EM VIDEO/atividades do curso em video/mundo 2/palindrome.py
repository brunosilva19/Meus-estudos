"""palindrome"""
palavra = input('Digite uma frase para saber se é palindrome: ').strip().upper()
nome = ''.join(palavra.split())
nome_contraio_com_laco = ''
NOME_CONTRARIO_SEM_LACO = nome[::-1]
for c in range(len(nome)-1,-1,-1):
    nome_contraio_com_laco += nome[c]
print(f'O inverso de {nome} é {nome_contraio_com_laco} = esse foi feito usando o laço')
print(f'O inverso de {nome} é {NOME_CONTRARIO_SEM_LACO} = esse foi feito sem usar o laço')
if nome_contraio_com_laco == nome:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
