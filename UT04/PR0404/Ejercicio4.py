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