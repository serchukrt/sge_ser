# Practica 4 - Ejercicios con diccionarios

### Ejercicios:

1.

```python

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
    print(f"El precio de la {fruta_buscada.capitalize()} es: €{precio:.2f}")
else:
     print(f"La fruta '{fruta_buscada.capitalize()}' no está disponible.")

```

2.

```python

productos = {
        "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
        "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
        "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
        "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
        "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
    }
num_categorias = len(productos)
print(f"Número de categorías: {num_categorias}")

print("Productos por categoría:")
total_productos = 0
for categoria, lista_productos in productos.items():
    num_productos_categoria = len(lista_productos)
    print(f"- {categoria}: {num_productos_categoria} productos")
    total_productos += num_productos_categoria

    print(f"Total de productos: {total_productos}")

```

3.

```python

frase = input("Introduce una frase: ")

frase_limpia = frase.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
palabras = frase_limpia.split()
frecuencias = {}

for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print("Frecuencia de palabras:")
for palabra, cuenta in frecuencias.items():
    print(f"'{palabra}': {cuenta}")

```

4.

```python

asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

while True:
    print("\n" + "="*30)
    print("         MENÚ DE GESTIÓN")
    print("="*30)
    print("1. Listar estudiantes (Ver una asignatura)")
    print("2. Matricular un estudiante")
    print("3. Dar de baja un estudiante")
    print("4. Salir")
    print("="*30)

    opcion = input("Elige una opción (1-4): ")

    if opcion == '4':
        print("Saliendo del programa. ¡Hasta pronto!")
        break
    
    if opcion in ('1', '2', '3'):
        asignatura = input("Nombre de la asignatura: ").capitalize()
        
        if asignatura not in asignaturas:
            print(f"La asignatura {asignatura} no existe. Inténtalo de nuevo.")
            continue

        estudiantes = asignaturas[asignatura]
        
        
        if opcion == '1':
            print(f"Estudiantes de {asignatura} ({len(estudiantes)} total):")
            if estudiantes:
                print(f"> {', '.join(estudiantes)}")
            else:
                print(f"{asignatura} no tiene estudiantes matriculados.")
        
        elif opcion == '2':
            estudiante = input("Nombre del estudiante a matricular: ").capitalize()
            if estudiante not in estudiantes:
                estudiantes.append(estudiante)
                print(f"{estudiante} matriculado en {asignatura}.")
            else:
                print(f"{estudiante} ya está matriculado en {asignatura}.")
        
        elif opcion == '3':
            estudiante = input("Nombre del estudiante a dar de baja: ").capitalize()
            if estudiante in estudiantes:
                estudiantes.remove(estudiante)
                print(f"{estudiante} dado de baja de {asignatura}.")
            else:
                print(f"{estudiante} no está en la lista de {asignatura}.")
    
    else:
        print("Opción no válida. Por favor, introduce un número del 1 al 4.")

```

5.

```python

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

```

6.

```python

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

```
