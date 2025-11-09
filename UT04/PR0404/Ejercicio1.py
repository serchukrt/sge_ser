frutas_precios = {
        "manzana": 1.20,
        "banana": 0.50,
        "naranja": 0.85,
        "uva": 3.50,
        "pera": 1.50
    }
fruta_buscada = input("Introduce el nombre de la fruta: ").lower()

if fruta_buscada in frutas_precios:
    precio = frutas_precios[fruta_buscada]
    print(f"El precio de la {fruta_buscada.capitalize()} es: ${precio:.2f}")
else:
     print(f"Lo sentimos, la fruta '{fruta_buscada.capitalize()}' no está disponible.")