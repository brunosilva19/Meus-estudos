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
    valor = float(input(''))
    porcentagem = float(input(''))
    print(f'{acrescimo(valor,porcentagem):.2f}')
    print(f'{desconto(valor, porcentagem):.2f}')

if __name__ == '__main__':
    main()
