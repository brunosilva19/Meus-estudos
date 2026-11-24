"""Módulo com funções para calcular desconto e acréscimo."""


def desconto(preco, porcentagem):
    """valor com desconto"""
    valor_desconto = preco - (preco * porcentagem) / 100
    return valor_desconto


def acrescimo(preco, porcentagem):
    """valor com acrescimo"""
    valor_acrescimo = preco + (preco * porcentagem) / 100
    return valor_acrescimo

def main():
    """ëntrada de dados"""
    valor = float(input('valor do produto: R$ '))
    porcentagem = float(input('porcentagem: '))
    print(f'O valor de R$ {valor:.2f} com {porcentagem:.2f}% de acrescimo fica : R$ {acrescimo(valor,porcentagem):.2f}')
    print(f'O valor de R$ {valor:.2f} com {porcentagem:.2f}% de desconto fica : R$ {desconto(valor, porcentagem):.2f}')

if __name__ == '__main__':
    main()
