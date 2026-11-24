def inverter(valor):
    """inverter numero"""
    return valor[::-1]


def main():
    """entrada de dados"""
    valor = input("")
    invertido = inverter(valor)
    print(invertido)

if __name__ == '__main__':
    main()
