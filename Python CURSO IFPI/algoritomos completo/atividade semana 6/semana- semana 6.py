def codigo_numerico(x):
    return chr(x)
def main():
    nome = input('Digite um caractere: ').strip()
    valor = codigo_numerico(nome)
    print('O código numérioco de {nome} é {valor}')
if __name__ == '__main__':
    main()
