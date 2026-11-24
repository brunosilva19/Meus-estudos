def codigo_numerico(x):
    codigo = ord(x)
    return codigo
def main():
    nome = input('')
    f = codigo_numerico(nome)
    print(f'{f}')
if __name__ == '__main__':
    main()
