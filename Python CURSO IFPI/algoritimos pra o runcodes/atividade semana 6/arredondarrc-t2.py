def arredondar_valor(valor):
    return round(valor)

def main():
    valor = float(input(""))
    resultado = arredondar_valor(valor)
    print(f"{resultado}")
if __name__ == '__main__':
    main()