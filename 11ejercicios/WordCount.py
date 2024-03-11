def contar_palabras(oracion):
    palabras = oracion.split()
    numero_palabras = len(palabras)
    return numero_palabras

def main():
    oracion_usuario = input("¿Qué tienes en mente hoy? ")
    palabras_oracion_usuario = contar_palabras(oracion_usuario)
    print(f"Oh, ¡qué bueno! ¡Acabas de decirme lo que tienes en mente en {palabras_oracion_usuario} palabras!")

    nombre_archivo = input("Por favor, introduce el nombre del archivo: ")
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras_archivo = contar_palabras(contenido)
            print(f"El archivo '{nombre_archivo}' tiene un total de {palabras_archivo} palabras.")
    except FileNotFoundError:
        print("El archivo no se encontró. Por favor, asegúrate de que el nombre del archivo sea correcto.")

if __name__ == "__main__":
    main()
