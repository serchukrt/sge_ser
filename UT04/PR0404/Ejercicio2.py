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