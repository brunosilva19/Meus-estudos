po_de_lua = int(input('Quanto de Pó de Lua Estelar você precisa: '))
essencia_de_dragao = int(input('Quanto de Essência de Dragão você precisa: '))
lagrima_de_fenix = int(input('Quanto de Lágrimas de Fênix você precisa: '))

valor_total = (po_de_lua * 5) + (essencia_de_dragao * 3) + (lagrima_de_fenix * 8)

print(f'Para fazer sua porção, você vai precisar de {valor_total} modedas de ouro.')
