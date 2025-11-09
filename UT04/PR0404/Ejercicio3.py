frase = input("Introduce una frase: ")

frase_limpia = frase.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
palabras = frase_limpia.split()
frecuencias = {}

for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print("Frecuencia de palabras:")
for palabra, cuenta in frecuencias.items():
    print(f"'{palabra}': {cuenta}")