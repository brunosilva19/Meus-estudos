def converter_temperatura(celsius):
    return (celsius * (9 / 5)) + 32


def main():
    celsius = float(input("Digite a temperatura em Celsius: "))

    fahrenheit = converter_temperatura(celsius)

    print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")
if __name__=="__main__":
    main()