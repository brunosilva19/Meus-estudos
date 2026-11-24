medida = float(input('Digite uma medida em metros: '))

km = medida / 1000
hm = medida / 100
dm = medida / 10
dc = medida * 10
cm = medida * 100
mm = medida * 1000

print(f'{km} km')
print(f'{hm} hm')
print(f'{dm} dam')
print(f'{dc:.0f} dm')
print(f'{cm:.0f} cm')
print(f'{mm:.0f} mm')
