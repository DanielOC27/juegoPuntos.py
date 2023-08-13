jugadores= {
            "daniel":0,
            "manuela":0
            }

historial = {
            "daniel": {"ganadas": [], "perdidas": []},
            "manuela": {"ganadas": [], "perdidas": []}
}

valores=(5,-2)

print("Bienvenido a Gana Puntos ")
print()
print("La tabla de puntajes se encuentra asi: \n",jugadores)

ronda=1
def guardarHistorial(nombre, resultado):
    if resultado.lower() == "ganar":
        historial[nombre]["ganadas"].append(ronda)
    elif resultado.lower() == "perder":
        historial[nombre]["perdidas"].append(ronda)


def actualizarPuntaje (nombre,resultado):
    if resultado.lower() == "ganar":
        jugadores[nombre] += valores[0]
    elif resultado.lower() == "perder":
        jugadores[nombre] += valores[1]
    else:
        print("Solo puedes ingresar (Ganar) o (Perder)")
    
    if jugadores[nombre] <-10:
        jugadores[nombre] = -10
    elif jugadores[nombre] >20:
        jugadores[nombre] = 20


def jugar (jugadores):
    nombre=input("Nombre del jugador : ")

    if nombre in jugadores:
        resultado=input("a continuación indica el resultado (Ganar) (Perder) : ")
        guardarHistorial(nombre, resultado)
        actualizarPuntaje(nombre, resultado)
        if  resultado.lower() == "ganar":
            jugadores[nombre] += 5

        elif resultado.lower() == "perder":
            jugadores[nombre] -= 1 
        else:
            print(" solo puede ingresa (Ganar) o (Perder)")
    else:
        print("jugador no valido")


def finJuego(jugadores, historial):
    print("Puntajes finales:")
    for jugador, puntaje in jugadores.items():
        print(f"{jugador}: {puntaje} puntos")

    for jugador, historial in historial.items():
        print(f"\nHistorial de {jugador}:")
        print("Rondas ganadas:", historial["ganadas"])
        print("Rondas perdidas:", historial["perdidas"])

ingreso = "si"

while(ingreso=="si"):
    print("Ronda #",ronda,":")
    jugar(jugadores)

    ingreso=input("¿Deseas jugar la siguiente ronda?(si)(no) ")
    ronda +=1

print()
print("Juego terminado.")
print()

finJuego(jugadores, historial)






    

