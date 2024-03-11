def obtener_acronimo(frase):
    acronimo = ''.join(word[0].upper() for word in frase.split())
    return acronimo

def main():
    frase_completa = input("Por favor, ingresa el significado completo de una organización o concepto: ")
    acronimo = obtener_acronimo(frase_completa)
    print("El acrónimo para", frase_completa, "es:", acronimo)

if __name__ == "__main__":
    main()
