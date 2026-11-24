# entra de dados
nome = input('Digite seu nome: ').strip()
idade = int(input('Digite sua idade: '))
preco = float(input('Valor do ingresso: R$ '))

# saida para o usuario
print(f'Cliente: {nome.title()}')

if idade <= 12 or idade >= 60:
    desconto = preco * 0.5
    txt = "com"
else:
    desconto = 0
    txt = "sem"
print(f'Desconto concedido: R$ {desconto:.2f}')
print(f'Valor do ingresso: R$ {preco - desconto:.2f}')
print(f'Cliente {txt} direito ao desconto!')
