def dados():
    return int(input('Digite um numero de termos: '))

def calculos(num):
    primeiro_termo = 0
    segundo_termo = 1
    count = 3
    
    print(f'{'SEQUÊNCIA FIBONACCI = '}', end='')
    
    print(f'{primeiro_termo} ➞  {segundo_termo} ➞  ',end='')
    
    while count <= num:
        
        terceiro_termo = primeiro_termo + segundo_termo
        print(f'{terceiro_termo}',end='')
        print(' ➞ ' if count < num else ' ➞  Fim',end=' ')
        primeiro_termo = segundo_termo
        segundo_termo = terceiro_termo
        count += 1
        
    print('')
    
def main():
    num = dados()
    calculos(num)

if __name__ == '__main__':
    main()