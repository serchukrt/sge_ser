original = {
    "España": "Madrid",
    "Francia": "París",
    "Alemania": "Berlín",
    "Italia": "Roma"
}

invertido = {}

print(f"Diccionario original: {original}")
print("-" * 30)

for clave_original, valor_original in original.items():
    invertido[valor_original] = clave_original

print(f"Diccionario invertido (Capitales a Países): {invertido}")