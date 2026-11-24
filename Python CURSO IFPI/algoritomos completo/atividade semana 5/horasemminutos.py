"""Converte uma quantidade de minutos para o formato horas:minutos."""


def calcular_horas(minutos):
    """Calcula a quantidade de horas a partir dos minutos informados."""
    return minutos // 60


def calcular_minutos(minutos):
    """Calcula os minutos restantes após a conversão para horas."""
    return minutos % 60


def main():
    """Solicita os minutos e exibe o resultado"""
    minutos = int(input("Digite a quantidade de minutos: "))
    horas = calcular_horas(minutos)
    minutos_restantes = calcular_minutos(minutos)
    print(f"{horas}:{minutos_restantes:02d}")


if __name__ == "__main__":
    main()
