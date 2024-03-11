import random

def jugar_adivina_el_numero():
    numero_secreto = random.randint(1, 50)
    intentos = 0
    
    while True:
        intento = input("Adivina el número secreto entre 1 y 50: ")

        try:
            intento = int(intento)
            if intento < 1 or intento > 50:
                print("Error: Por favor, elige un número dentro del rango correcto (1-50).")
                continue
            
            intentos += 1
            if intento < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"Felicidades, ¡adivinaste el número secreto {numero_secreto} en {intentos} intentos!")
                break

            continuar = input("¿Quieres seguir jugando? (sí/no): ").lower()
            if continuar != 'si':
                print("¡Gracias por jugar!")
                break
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")

def main():
    print("Bienvenido al juego Adivina el Número!")
    jugar_adivina_el_numero()

if __name__ == "__main__":
    main()
