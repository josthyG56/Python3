import requests;

canciones = {
    "Justin Bieber": ["Baby", "Sorry", "Love Yourself"],
    "Drake": ["Hotline Bling", "God's Plan", "In My Feelings"],
    "Beyonce": ["Flawless", "Single Ladies", "Halo"],
    "Eminem": ["Lose Yourself", "Stan", "Love the Way You Lie"]
}

def mostrar_menu():
    print("Bienvenido, por favor elija una canción de estas 10 canciones:\n")
    numero = 1
    for artista, lista_canciones in canciones.items():
        for cancion in lista_canciones:
            print(f"{numero}. {cancion} de {artista}")
            numero += 1

def seleccionar_cancion():
    seleccion = input("\nPor favor, ingrese el número de la canción que elija (o * para elegir nuevamente): ")
    if seleccion == "*":
        mostrar_menu()
        seleccionar_cancion()
    elif seleccion.isdigit():
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(canciones) * 3:
            return seleccion
        else:
            print("Entrada no válida. Por favor, ingrese un número válido.")
            seleccionar_cancion()
    else:
        print("Entrada no válida. Por favor, ingrese un número válido.")
        seleccionar_cancion()

def obtener_letra(artista, cancion):
    url = f"https://api.lyrics.ovh/v1/{artista}/{cancion}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        data = respuesta.json()
        if 'lyrics' in data:
            return data['lyrics']
    return "Lo siento, la letra de esta canción no está disponible."

def main():
    mostrar_menu()
    seleccion = seleccionar_cancion()
    index_cancion = (seleccion - 1) % 3
    index_artista = (seleccion - 1) // 3
    artista = list(canciones.keys())[index_artista]
    cancion = canciones[artista][index_cancion]
    letra = obtener_letra(artista, cancion)
    print(f"\n------ {cancion} by {artista} ------\n{letra}")
    if input("\nPresione * para elegir nuevamente: ") == "*":
        main()

if __name__ == "__main__":
    main()
