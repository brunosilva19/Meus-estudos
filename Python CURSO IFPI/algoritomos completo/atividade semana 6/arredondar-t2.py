def arredondar_valor(valor):
    return round(valor)

def main():
    valor = float(input("Digite uma quantidade de dinheiro: R$ "))
    resultado = arredondar_valor(valor)
    print(f"Valor arredondado: R$ {resultado}")
if __name__=="__main__":
    main()