def es_palindromo(palabra):
    return palabra == palabra[::-1]

def main():
    palabras = []
    for i in range(5):
        palabra = input(f"Ingrese la palabra {i+1}: ").lower()
        palabras.append(palabra)

    palindromos = []
    for palabra in palabras:
        if es_palindromo(palabra):
            palindromos.append(palabra)

    if palindromos:
        print("Las siguientes palabras son palíndromos:")
        for palindromo in palindromos:
            print("-", palindromo)
    else:
        print("Ninguna de las palabras ingresadas es un palíndromo.")

if __name__ == "__main__":
    main()
