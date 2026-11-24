def dados():
    valor_carro = float(input('Digite o valor do carro: R$ '))
    return valor_carro

def calcular_dados(valor_carro):
    banco = 10000
    meses = 0
    
    while banco <= valor_carro:
        meses += 1
        banco += (banco * 0.007)
        valor_carro += (valor_carro * 0.004)
        
    return meses, banco
    
def main():
    valor_carro = dados()
    meses, banco = calcular_dados(valor_carro)
    print(f'Com o valor de R$ 10.000,00 com aumento de 0,7% ao ano temos: R$ {banco:.2f}.\nVamos precisar de {meses} mes para compra o carro.')

if __name__ == '__main__':
    main()