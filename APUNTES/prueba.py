info = input("Ingrese su ciclo: ")
msg = (
    "Desarrollo de aplicaciones multiplataforma" if info == "DAM" else
    "Desarrollo de aplicaciones web" if info == "DAW" else
    "Administracion de sistemas en red" if info == "ASIR" else
    "No existe el ciclo ingresado"
)
print(msg)