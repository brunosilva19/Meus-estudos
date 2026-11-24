def ops(valor):
    return valor in ('V', 'A', 'E')
def main():
    valor = input("""=========================
[V] VERDE
[A] AMARELO
[E] VERMELHO 

Digite apenas [V] , [A] , [E]: """).strip().upper()
    print('=========================')
    if ops(valor):  
        if valor == 'V':
            print('Siga')
        elif valor == 'A':
            print('Atenção')
        else:
            print('Pare')
    else:
        print('Opção inválida!')
if __name__ == '__main__':
    main()