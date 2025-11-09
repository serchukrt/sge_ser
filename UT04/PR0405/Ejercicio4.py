palabras = ["perro", "gato", "elefante", "oso", "jirafa"]
palabras_largas = filter(lambda p: len(p) > 5, palabras)
palabras_largas_mayusculas = list(map(lambda p: p.upper(), palabras_largas))
print(palabras_largas_mayusculas)