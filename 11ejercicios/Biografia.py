import re

def validar_nombre(nombre):
    if re.match("^[A-Za-z ]+$", nombre):
        return True
    else:
        return False

def validar_fecha(fecha):
    if re.match("^[A-Za-z]+ [0-9]{1,2}, [0-9]{4}$", fecha):
        return True
    else:
        return False

def validar_direccion(direccion):
    if re.match("^[A-Za-z0-9, ]+$", direccion):
        return True
    else:
        return False

def solicitar_informacion():
    nombre = input("¿Cuál es tu nombre? ")
    while not validar_nombre(nombre):
        print("Por favor, ingresa un nombre válido.")
        nombre = input("¿Cuál es tu nombre? ")

    fecha_nacimiento = input("¿Cuál es tu fecha de nacimiento? (Ejemplo: Jun 1, 1954) ")
    while not validar_fecha(fecha_nacimiento):
        print("Por favor, ingresa una fecha de nacimiento válida en el formato correcto.")
        fecha_nacimiento = input("¿Cuál es tu fecha de nacimiento? (Ejemplo: Jan 1, 1954) ")

    direccion = input("¿Cuál es tu dirección? ")
    while not validar_direccion(direccion):
        print("Por favor, ingresa una dirección válida.")
        direccion = input("¿Cuál es tu dirección? ")

    metas_personales = input("¿Cuáles son tus metas personales? ")

    return nombre, fecha_nacimiento, direccion, metas_personales

def imprimir_resumen(nombre, fecha_nacimiento, direccion, metas_personales):
    print("\nResumen de tu información personal:")
    print("- Nombre:", nombre)
    print("- Fecha de nacimiento:", fecha_nacimiento)
    print("- Direccion:", direccion)
    print("- Metas:", metas_personales)

def main():
    nombre, fecha_nacimiento, direccion, metas_personales = solicitar_informacion()
    imprimir_resumen(nombre, fecha_nacimiento, direccion, metas_personales)

if __name__ == "__main__":
    main()
