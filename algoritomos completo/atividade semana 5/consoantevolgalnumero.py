valor = input('Digite algum para saber se é consoante ou não: ').lower()
yes = valor in 'abcdefghijklmnopqrstuvwxyz' or valor in str('0,1,2,3,4,5,6,7,8,8,9')
print(bool(yes))