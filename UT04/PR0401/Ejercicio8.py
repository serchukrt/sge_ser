mj1 = 0
mj2 = 0

while mj1 < 5 and mj2 < 5:
    j1 = input("Di la elección del jugador 1: ").lower()
    j2 = input("Di la elección del jugador 2: ").lower()

    match j1:
        case "piedra":
            if j2 in ["lagarto", "tijeras"]:
                res = "Gana jugador 1"
                mj1 += 1
            elif j2 in ["papel", "spok"]:
                res = "Gana jugador 2"
                mj2 += 1
            else:
                res = "Empate"

        case "papel":
            if j2 in ["piedra", "spok"]:
                res = "Gana jugador 1"
                mj1 += 1
            elif j2 in ["tijeras", "lagarto"]:
                res = "Gana jugador 2"
                mj2 += 1
            else:
                res = "Empate"

        case "tijeras":
            if j2 in ["papel", "lagarto"]:
                res = "Gana jugador 1"
                mj1 += 1
            elif j2 in ["piedra", "spok"]:
                res = "Gana jugador 2"
                mj2 += 1
            else:
                res = "Empate"

        case "lagarto":
            if j2 in ["spok", "papel"]:
                res = "Gana jugador 1"
                mj1 += 1
            elif j2 in ["tijeras", "piedra"]:
                res = "Gana jugador 2"
                mj2 += 1
            else:
                res = "Empate"

        case "spok":
            if j2 in ["tijeras", "piedra"]:
                res = "Gana jugador 1"
                mj1 += 1
            elif j2 in ["lagarto", "papel"]:
                res = "Gana jugador 2"
                mj2 += 1
            else:
                res = "Empate"

        case _:
            res = "Jugada no válida del jugador 1"

    print(res)
    print("Jugador 1:", mj1, "| Jugador 2:", mj2)

print("Jugador 1 gana la partida" if mj1 == 5 else "Jugador 2 gana la partida")
