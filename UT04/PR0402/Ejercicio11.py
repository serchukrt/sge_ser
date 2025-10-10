a = input("Introduce una frase: ")
palabras = a.replace("-", " ").split()
res = palabras[0].lower() + "".join(letra.capitalize() for letra in palabras[1:])
print(res)