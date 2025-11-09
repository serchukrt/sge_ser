tienda_a = {"leche": 1.50, "pan": 2.00, "huevos": 3.00, "queso": 4.50}
tienda_b = {"pan": 1.80, "huevos": 3.20, "jamon": 5.00, "leche": 1.40}

combinado = tienda_a.copy()

print(f"Tienda A: {tienda_a}")
print(f"Tienda B: {tienda_b}")
print("-" * 30)

for producto, precio_b in tienda_b.items():
    if producto in combinado:
        combinado[producto] += precio_b
    else:
        combinado[producto] = precio_b

print("\nDiccionario Combinado Final:")
print(combinado)