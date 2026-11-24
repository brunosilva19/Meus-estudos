"""Programa para calcular o valor da conta de um restaurante."""

# Entrada do usuário

valor_consumido = float(input('Valor da conta: R$ '))
taxa_de_servico = int(input('Taxa de serviço: '))
quantidade_de_pessoas = int(input('Quantidade de pessoas: '))

taxa = valor_consumido * taxa_de_servico/100
total_conta = valor_consumido + taxa
valor_por_pessoa = total_conta/quantidade_de_pessoas


print(f'A taxa de serviço é de: R$ {taxa:.2f}.')
print(f'O total da conta é de: R$ {total_conta:.2f}.')
print(f'O valor por pessoa é de: R$ {valor_por_pessoa:.2f}.')
