morango_kg = float(input("").replace(",", "."))
maca_kg = float(input("").replace(",", "."))

preco_morango = 2.20 if morango_kg > 5 else 2.50
preco_maca = 1.50 if maca_kg > 5 else 1.80

total = morango_kg * preco_morango + maca_kg * preco_maca

if morango_kg + maca_kg > 8 or total > 25:
	total *= 0.90

print(f"{total:.2f}")
