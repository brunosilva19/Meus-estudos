valor = input('Digite algum para saber se é consoante ou não: ').lower()
yes = valor in 'bcdfghjklmnpqrstvwxz'
print(bool(yes))