def converter_temperatura(celsius):
    return (celsius * (9 / 5)) + 32


def main():
    celsius = float(input(""))

    fahrenheit = converter_temperatura(celsius)

    print(f"{fahrenheit:.2f}")


main()