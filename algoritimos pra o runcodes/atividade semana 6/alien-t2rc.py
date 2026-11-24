from math import floor

def converter_idade(idade):
    return idade / 2

def main():
    idade = int(input(""))

    idade_espacial = floor(converter_idade(idade))

    print(f"{idade_espacial}")

main()