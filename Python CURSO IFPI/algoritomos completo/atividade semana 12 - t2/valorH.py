def dados():
    return int(input('Digite um valor: '))

def calculos(num):
    
    count = 2
    valor = 1
    
    while count <= num:
        valor +=  ( 1 / count)
        count += 1
    
    return valor

def main():
    num = dados()
    valor = calculos(num)
    print('=' * 40)
    print(f'O valor é de: {valor:.4f}')
    print('=' * 40)
if __name__ == '__main__':
    main()