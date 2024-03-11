import random

def jugar_piedra_papel_tijeras(jugador, computadora):
    if jugador == computadora:
        return "¡Es un empate!"
    elif (jugador == 1 and computadora == 3) or (jugador == 2 and computadora == 1) or (jugador == 3 and computadora == 2):
        return "¡Felicidades! ¡Ganaste!"
    else:
        return "¡Oh no! ¡La computadora ganó!"

def main():
    opciones = {1: "piedra", 2: "papel", 3: "tijeras"}
    while True:
        print("Elige una opción:")
        print("1) Piedra")
        print("2) Papel")
        print("3) Tijeras")
        print("4) Salir")
        jugador = input("Tu elección: ")
        
        if jugador == '4':
            print("¡Gracias por jugar! ¡Hasta luego!")
            break

        try:
            jugador = int(jugador)
            if jugador in opciones:
                computadora = random.randint(1, 3)
                resultado = jugar_piedra_papel_tijeras(jugador, computadora)
                print("Tú elegiste:", opciones[jugador])
                print("La computadora eligió:", opciones[computadora])
                print(resultado)
            else:
                print("Por favor, elige una opción válida.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()

