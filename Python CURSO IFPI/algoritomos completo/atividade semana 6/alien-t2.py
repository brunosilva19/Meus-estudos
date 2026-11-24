from math import floor
def converter_idade(idade):
    return idade / 2

def main():
    idade = float(input("Digite a idade em anos terrestres: "))

    idade_espacial = floor(converter_idade(idade))

    print(f"Idade em anos espaciais: {idade_espacial}")
if __name__=="__main__":
    main()