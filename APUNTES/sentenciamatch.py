a = input("Dime que ciclo estas estudiando: ")
match a:
    case "DAM":
        print("Desarrollo de Aplicaciones Multiplataforma")
    case "DAW":
        print("Desarrollo de Aplicaciones Web")
    case "ASIR":
        print("Sistemas en Res")
    case _:
        print("No lo conozco")