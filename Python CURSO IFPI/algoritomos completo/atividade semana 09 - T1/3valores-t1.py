def menor_diferenca(prim, seg, ter):
    
    diff_seg = abs(seg - prim)
    diff_ter = abs(ter - prim)
 
    return min(diff_seg, diff_ter)

def main():
   
    prim = int(input('Digite o primero valor: '))
    seg = int(input('Digite o segundo valor: '))
    ter = int(input('Digite o terceiro valor: '))

    print(menor_diferenca(prim, seg, ter))
    
if __name__ == "__main__":
    main()
